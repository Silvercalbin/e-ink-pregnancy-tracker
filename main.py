#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
Main script with smart e-ink refresh logic

Features:
- Daily refresh at midnight
- Progress refresh at 0.1% steps (06–22h, start page only)
- Weekly full clear (Sunday 04:00+)
"""
import json
import os
import time
import logging
import signal
import sys
import datetime

logging.basicConfig(level=logging.WARNING)

# Load config
config_file_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'config.json'
)
config = json.load(open(config_file_path))

# Globals
epd = None
screen_ui = None
pregnancy = None

def cleanup_and_exit(signum=None, frame=None):
    global epd
    if epd:
        try:
            epd.sleep()
        except:
            pass
    sys.exit(0)

def update_display(page_num):
    global epd, screen_ui
    try:
        screen_ui.set_page(page_num)
        himage = screen_ui.draw()
        epd.display(epd.getbuffer(himage))
    except Exception as e:
        logging.error(f"Display update error: {e}")

signal.signal(signal.SIGINT, cleanup_and_exit)
signal.signal(signal.SIGTERM, cleanup_and_exit)

try:
    # 🖥 DISPLAY INIT
    from waveshare_epd import epd2in7_V2
    epd = epd2in7_V2.EPD()
    epd.init()
    epd.Clear()

    # 🤰 LOGIC INIT
    from pregnancy_tracker import ScreenUI, Pregnancy
    pregnancy = Pregnancy(config['expected_birth_date'])
    screen_ui = ScreenUI(epd.height, epd.width, pregnancy, current_page=0)

    # Initial draw
    update_display(0)

    # State tracking
    last_date = datetime.date.today()
    last_progress = round(pregnancy.get_progress() * 100, 1)
    # Set last_full_clear_week to last week, to ensure clear triggers
    last_full_clear_week = datetime.date.today().isocalendar()[1] - 1

    # 🎛 BUTTON SETUP
    try:
        import RPi.GPIO as GPIO

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        buttons = {1: 5, 2: 6, 3: 13, 4: 19}
        for pin in buttons.values():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        button_states = {b: 1 for b in buttons}
        last_press_time = 0

        while True:
            now = datetime.datetime.now()
            today = now.date()

            # 🕛 DAILY REFRESH (ALWAYS)
            if today != last_date:
                logging.warning("New day detected – daily refresh")
                update_display(screen_ui.current_page)
                last_date = today

            # 📊 PROGRESS REFRESH (06–22, start page only)
            if (
                screen_ui.current_page == 0 and
                6 <= now.hour <= 22
            ):
                current_progress = round(
                    pregnancy.get_progress() * 100, 1
                )
                if current_progress != last_progress:
                    logging.warning(
                        f"Progress changed: {last_progress}% → {current_progress}%"
                    )
                    update_display(0)
                    last_progress = current_progress

            # 🧹 WEEKLY FULL CLEAR (Sunday 04:00+)
            current_week = today.isocalendar()[1]
            if (
                now.weekday() == 6 and  # Sonntag
                now.hour >= 4 and       # ab 04:00 Uhr
                current_week != last_full_clear_week
            ):
                logging.warning(
                    f"Weekly full clear triggered: weekday={now.weekday()}, "
                    f"hour={now.hour}, current_week={current_week}, "
                    f"last_full_clear_week={last_full_clear_week}"
                )
                epd.Clear()
                update_display(screen_ui.current_page)
                last_full_clear_week = current_week

            # 🔘 BUTTON HANDLING
            for btn, pin in buttons.items():
                state = GPIO.input(pin)
                if state == 0 and button_states[btn] == 1:
                    now_ts = time.time()
                    if now_ts - last_press_time > 1:
                        last_press_time = now_ts
                        update_display(btn - 1)
                button_states[btn] = state

            time.sleep(0.05)

    except ImportError:
        # Headless mode
        while True:
            time.sleep(1)

except Exception as e:
    logging.error(f"Fatal error: {e}")
    import traceback
    traceback.print_exc()
    cleanup_and_exit()
