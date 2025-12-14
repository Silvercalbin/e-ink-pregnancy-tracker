# Size comparisons for different pregnancy weeks
# Format: week -> (size comparison, length in cm/inches)

PREGNANCY_SIZES = {
    4: ("Poppy seed", "0.2 cm"),
    5: ("Sesame seed", "0.3 cm"),
    6: ("Lentil", "0.6 cm"),
    7: ("Blueberry", "1 cm"),
    8: ("Raspberry", "1.6 cm"),
    9: ("Grape", "2.3 cm"),
    10: ("Kumquat", "3.1 cm"),
    11: ("Laubfrosch", "4.1 cm"),
    12: ("Pflaume", "5.4 cm"),
    13: ("Zitrone", "6.7 cm"),
    14: ("Pfirsich", "14.7 cm"),
    15: ("Apfel", "16.7 cm"),
    16: ("Avocado", "18.6 cm"),
    17: ("Granatapfel", "20.4 cm"),
    18: ("Paprika", "22.2 cm"),
    19: ("Mango", "24.0 cm"),
    20: ("Banane", "25.7 cm"),
    21: ("Ofenkartoffel", "27.4 cm"),
    22: ("Maiskolben", "29 cm"),
    23: ("Grapefruit", "30.6 cm"),
    24: ("Aubergine", "32.2 cm"),
    25: ("Weintraube", "33.7 cm"),
    26: ("Steckrübe", "35.1 cm"),
    27: ("Blumenkohl", "36.6 cm"),
    28: ("Kokosnuss", "37.9 cm"),
    29: ("Butternut-Kürbis", "39.2 cm"),
    30: ("Spitzkohl", "40.5 cm"),
    31: ("Zucchini", "41.8 cm"),
    32: ("Bündel Sellerie", "43 cm"),
    33: ("Ananas", "44 cm"),
    34: ("Cantaloupe-Melon", "45.2 cm"),
    35: ("Honigmelone", "46.3 cm"),
    36: ("Wirsing", "47.3 cm"),
    37: ("Lauch", "48.3 cm"),
    38: ("Papaya", "49.2 cm"),
    39: ("Speisekürbis", "50.1 cm"),
    40: ("Kürbis", "51.0 cm"),
}

def get_size_for_week(week):
    """Get the size comparison for a given pregnancy week"""
    if week < 4:
        return ("Zu früh", "< 0.2 cm")
    elif week > 40:
        return ("Voll entwickelt", "~51 cm")
    else:
        return PREGNANCY_SIZES.get(week, ("Growing", f"~{10 + (week-10)*1.5:.1f} cm"))
