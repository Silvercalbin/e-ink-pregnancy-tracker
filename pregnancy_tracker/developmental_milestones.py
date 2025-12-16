"""Developmental milestones and anatomy updates for each week of pregnancy."""

def get_milestone_for_week(week):
    """Get developmental milestone information for a specific week.
    
    Returns:
        dict: Contains 'size', 'weight', and 'development' keys with milestone info
    """
    
    milestones = {
        4: {
            "size": "Poppy seed",
            "weight": "< 1g",
            "development": "Neuralrohr bildet sich, Herz beginnt sich zu entwickeln"
        },
        5: {
            "size": "Sesame seed",
            "weight": "< 1g",
            "development": "Herz beginnt zu schlagen, Arm- und Beinansätze entstehen"
        },
        6: {
            "size": "Lentil",
            "weight": "< 1g",
            "development": "Augen und Ohren bilden sich, Kiefer und Rachen entwickeln sich"
        },
        7: {
            "size": "Blueberry",
            "weight": "< 1g",
            "development": "Gehirnhälften entstehen, Arme und Beine wachsen"
        },
        8: {
            "size": "Kidney bean",
            "weight": "1g",
            "development": "Finger und Zehen bilden sich, Augenlider entwickeln sich"
        },
        9: {
            "size": "Grape",
            "weight": "2g",
            "development": "Wichtige Organe sind angelegt, Ellbogen und Zehen sichtbar"
        },
        10: {
            "size": "Kumquat",
            "weight": "35g",
            "development": "Lebenswichtige Organe funktionieren, Zahnknospen entstehen"
        },
        11: {
            "size": "Fig",
            "weight": "45g",
            "development": "Knochen verhärten sich, feine Körperhaare entwickeln sich"
        },
        12: {
            "size": "Lime",
            "weight": "58g",
            "development": "Reflexe beginnen, Nieren produzieren Urin"
        },
        13: {
            "size": "Peapod",
            "weight": "73g",
            "development": "Fingerabdrücke entstehen, Stimmbänder entwickeln sich"
        },
        14: {
            "size": "Lemon",
            "weight": "93g",
            "development": "Gesichtsmuskeln arbeiten, kann blinzeln und Grimassen machen"
        },
        15: {
            "size": "Apple",
            "weight": "117g",
            "development": "Beine sind länger als Arme, alle Gelenke funktionieren"
        },
        16: {
            "size": "Avocado",
            "weight": "146g",
            "development": "Kann Geräusche hören, Augen bewegen sich seitlich"
        },
        17: {
            "size": "Turnip",
            "weight": "181g",
            "development": "Skelett verhärtet sich, Schweißdrüsen entwickeln sich"
        },
        18: {
            "size": "Bell pepper",
            "weight": "223g",
            "development": "Ohren erreichen ihre endgültige Position, Nerven werden geschützt"
        },
        19: {
            "size": "Heirloom tomato",
            "weight": "273g",
            "development": "Sinnesentwicklung, Käseschmiere (Vernix caseosa) bildet sich"
        },
        20: {
            "size": "Banana",
            "weight": "331g",
            "development": "Kann schlucken, erstes Kindspech (Mekonium) entsteht"
        },
        21: {
            "size": "Carrot",
            "weight": "399g",
            "development": "Augenbrauen und Augenlider vollständig, reagiert auf Geräusche"
        },
        22: {
            "size": "Spaghetti squash",
            "weight": "478g",
            "development": "Augen können Licht wahrnehmen, Greifkraft nimmt zu"
        },
        23: {
            "size": "Mango",
            "weight": "568g",
            "development": "Gehör vollständig entwickelt, schnelle Augenbewegungen"
        },
        24: {
            "size": "Corn cob",
            "weight": "670g",
            "development": "Lunge bildet Verzweigungen, Geschmacksknospen entstehen"
        },
        25: {
            "size": "Rutabaga",
            "weight": "785g",
            "development": "Reagiert auf Stimmen, Nasenlöcher öffnen sich"
        },
        26: {
            "size": "Scallion bunch",
            "weight": "913g",
            "development": "Augen öffnen sich, Ein- und Ausatmen von Fruchtwasser"
        },
        27: {
            "size": "Cauliflower",
            "weight": "1.06kg",
            "development": "Gehirngewebe entwickelt sich, regelmäßige Schlafzyklen"
        },
        28: {
            "size": "Eggplant",
            "weight": "1.21kg",
            "development": "Kann blinzeln, träumt während des REM-Schlafs"
        },
        29: {
            "size": "Butternut squash",
            "weight": "1.37kg",
            "development": "Muskeln und Lunge reifen, Kopf wächst"
        },
        30: {
            "size": "Large cabbage",
            "weight": "1.55kg",
            "development": "Bildung roter Blutkörperchen, schnelles Gehirnwachstum"
        },
        31: {
            "size": "Coconut",
            "weight": "1.75kg",
            "development": "Alle fünf Sinne funktionieren, verarbeitet Reize"
        },
        32: {
            "size": "Jicama",
            "weight": "1.95kg",
            "development": "Knochen verhärten sich weiter, Atembewegungen werden geübt"
        },
        33: {
            "size": "Pineapple",
            "weight": "2.16kg",
            "development": "Immunsystem entwickelt sich, erkennt Licht"
        },
        34: {
            "size": "Cantaloupe",
            "weight": "2.37kg",
            "development": "Zentrales Nervensystem reift, erkennt bekannte Lieder"
        },
        35: {
            "size": "Honeydew melon",
            "weight": "2.59kg",
            "development": "Nieren vollständig entwickelt, Leber verarbeitet Abfallstoffe"
        },
        36: {
            "size": "Romaine lettuce",
            "weight": "2.81kg",
            "development": "Lanugo (feine Körperhaare) werden abgestoßen, Verdauung bereit"
        },
        37: {
            "size": "Swiss chard",
            "weight": "3.02kg",
            "development": "Termingerecht, übt Atmen und Saugen"
        },
        38: {
            "size": "Leek",
            "weight": "3.23kg",
            "development": "Organe ausgereift, Gehirn und Nervensystem bereit"
        },
        39: {
            "size": "Mini watermelon",
            "weight": "3.43kg",
            "development": "Vollständig entwickelt, Fettreserven werden aufgebaut"
        },
        40: {
            "size": "Small pumpkin",
            "weight": "3.61kg",
            "development": "Bereit für die Geburt, alle Systeme funktionsfähig"
        }
    }
    
    # Handle weeks outside normal range
    if week < 4:
        return {
            "size": "Poppy seed",
            "weight": "< 1g",
            "development": "Zellen teilen sich schnell, Einnistung findet statt"
        }
    elif week > 40:
        return {
            "size": "Kürbis",
            "weight": "3.5kg+",
            "development": "Voll entwickelt, bereit für die Geburt"
        }
    
    return milestones.get(week, milestones[40])
