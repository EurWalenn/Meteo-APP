import json
from Graphiques import func_creation_graphique_temp_vent
from Graphiques import func_creation_graphique_direction_vent_12h
from Graphiques import func_creation_graphique_direction_vent_14j
from Graphiques import func_creation_graphique_condition_meteo

def func_decode_data_actuelles_json(data):
    """
    Fonction pour décoder et afficher les données météorologiques actuelles.

    :param data: Les données JSON en entrée.
    :return: Aucune valeur de retour.
    """
    decoded_data = json.loads(json.dumps(data))  # Convertit les données JSON en un dictionnaire Python.

    # Affiche des informations sur la station météo et l'heure de l'observation.
    station = decoded_data[0]['station']['name']
    heure = decoded_data[0]['observation']['time']

    # Extrait les données météorologiques actuelles du dictionnaire.
    temperature = decoded_data[0]['observation']['temperature']['value']
    humidity = decoded_data[0]['observation']['humidity']['value']
    rainfall = decoded_data[0]['observation']['rainfall']['value']
    atmospheric_pressure = decoded_data[0]['observation']['atmospheric_pressure']['value']
    wind_s = decoded_data[0]['observation']['wind_s']['value']
    wind_direction_s = decoded_data[0]['observation']['wind_direction_s']['value']
    windgust_s = decoded_data[0]['observation']['windgust_s']['value']

    # Affiche les données météorologiques actuelles.
    print(f"Bulletin Météo de la station météo {station} à {heure}.")
    print(f"Temperature actuelle : {temperature}°C.")
    print(f"Humidité actuelle : {humidity}%.")
    print(f"Pluviométrie actuelle : {rainfall}mm.")
    print(f"Pression atmosphérique actuelle : {atmospheric_pressure}hPa.")
    print(f"Vent moyen = {wind_s}km/h.")
    print(f"Direction du vent moyen : {wind_direction_s}°.")
    print(f"Rafales de vent : {windgust_s}km/h.")

def func_decode_data_futures_12h(data, ZoneMeteo, PeriodeBulletin):
    """
    Fonction pour décoder et afficher les prévisions météorologiques pour les 12 prochaines heures.
    :param data: Les données JSON en entrée.
    :param ZoneMeteo: La zone météorologique.
    :param PeriodeBulletin: La période du bulletin.
    :return: Aucune valeur de retour.
    """
    decoded_data = json.loads(json.dumps(data))  # Convertit les données JSON en un dictionnaire Python.

    print(f"Bulletin météo prévisionnel de {ZoneMeteo} pour les {PeriodeBulletin}.")

    # Dictionnaire de codes météorologiques pour les descriptions.
    WEATHER = {
        0: "Soleil",
        1: "Peu nuageux",
        2: "Ciel voilé",
        3: "Nuageux",
        4: "Très nuageux",
        5: "Couvert",
        6: "Brouillard",
        7: "Brouillard givrant",
        10: "Pluie faible",
        11: "Pluie modérée",
        12: "Pluie forte",
        13: "Pluie faible verglaçante",
        14: "Pluie modérée verglaçante",
        15: "Pluie forte verglaçante",
        16: "Bruine",
        20: "Neige faible",
        21: "Neige modérée",
        22: "Neige forte",
        30: "Pluie et neige mêlées faibles",
        31: "Pluie et neige mêlées modérées",
        32: "Pluie et neige mêlées fortes",
        40: "Averses de pluie locales et faibles",
        41: "Averses de pluie locales",
        42: "Averses locales et fortes",
        43: "Averses de pluie faibles",
        44: "Averses de pluie",
        45: "Averses de pluie fortes",
        46: "Averses de pluie faibles et fréquentes",
        47: "Averses de pluie fréquentes",
        48: "Averses de pluie fortes et fréquentes",
        60: "Averses de neige localisées et faibles",
        61: "Averses de neige localisées",
        62: "Averses de neige localisées et fortes",
        63: "Averses de neige faibles",
        64: "Averses de neige",
        65: "Averses de neige fortes",
        66: "Averses de neige faibles et fréquentes",
        67: "Averses de neige fréquentes",
        68: "Averses de neige fortes et fréquentes",
        70: "Averses de pluie et neige mêlées localisées et faibles",
        71: "Averses de pluie et neige mêlées localisées",
        72: "Averses de pluie et neige mêlées localisées et fortes",
        73: "Averses de pluie et neige mêlées faibles",
        74: "Averses de pluie et neige mêlées",
        75: "Averses de pluie et neige mêlées fortes",
        76: "Averses de pluie et neige mêlées faibles et nombreuses",
        77: "Averses de pluie et neige mêlées fréquentes",
        78: "Averses de pluie et neige mêlées fortes et fréquentes",
        100: "Orages faibles et locaux",
        101: "Orages locaux",
        102: "Orages fort et locaux",
        103: "Orages faibles",
        104: "Orages",
        105: "Orages forts",
        106: "Orages faibles et fréquents",
        107: "Orages fréquents",
        108: "Orages forts et fréquents",
        120: "Orages faibles et locaux de neige ou grésil",
        121: "Orages locaux de neige ou grésil",
        122: "Orages locaux de neige ou grésil",
        123: "Orages faibles de neige ou grésil",
        124: "Orages de neige ou grésil",
        125: "Orages de neige ou grésil",
        126: "Orages faibles et fréquents de neige ou grésil",
        127: "Orages fréquents de neige ou grésil",
        128: "Orages fréquents de neige ou grésil",
        130: "Orages faibles et locaux de pluie et neige mêlées ou grésil",
        131: "Orages locaux de pluie et neige mêlées ou grésil",
        132: "Orages fort et locaux de pluie et neige mêlées ou grésil",
        133: "Orages faibles de pluie et neige mêlées ou grésil",
        134: "Orages de pluie et neige mêlées ou grésil",
        135: "Orages forts de pluie et neige mêlées ou grésil",
        136: "Orages faibles et fréquents de pluie et neige mêlées ou grésil",
        137: "Orages fréquents de pluie et neige mêlées ou grésil",
        138: "Orages forts et fréquents de pluie et neige mêlées ou grésil",
        140: "Pluies orageuses",
        141: "Pluie et neige mêlées à caractère orageux",
        142: "Neige à caractère orageux",
        210: "Pluie faible intermittente",
        211: "Pluie modérée intermittente",
        212: "Pluie forte intermittente",
        220: "Neige faible intermittente",
        221: "Neige modérée intermittente",
        222: "Neige forte intermittente",
        230: "Pluie et neige mêlées",
        231: "Pluie et neige mêlées",
        232: "Pluie et neige mêlées",
        235: "Averses de grêle",
    }

    heures = []
    vent_moyen = []
    rafale_vent = []
    temperature = []
    direction_vent = []
    prevision_meteo = []

    # Parcourt les prévisions météoroligiques
    for forecast_item in decoded_data.get("forecast", []):

        # Récupération de la date et l'heure de la prévision
        DateHeureOriginal = forecast_item.get('datetime', '')

        date_part, heure_part = DateHeureOriginal.split('T')
        date_universelle = date_part
        heure_universelle = heure_part[:5]
        DateHeure = f"{date_universelle} {heure_universelle}"

        # Récupération de la température de la prévision
        Temperature = forecast_item.get('temp2m', '')

        # Récupération de la vitesse du vent moyen de la prévision
        VentMoyen = forecast_item.get('wind10m', '')

        # Récupération de la vitesse des rafales de vent de la prévision
        RafaleVent = forecast_item.get('gust10m', '')

        # Récupération de la direction du vent de la prévision
        DirectionVent = forecast_item.get('dirwind10m', '')

        # Récupération du code météo de la prévision
        CodeMeteo = forecast_item.get('weather', '')
        # Conversion du code météo en description détaillée
        DescriptionMeteo = WEATHER.get(CodeMeteo, 'Inconnu')

        # Récupération de la probabilité des vents au-dessus de 70km/h
        ProbaVent70 = forecast_item.get('probawind70', '')

        # Récupération de la probabilité des vents au-dessus de 100km/h
        ProbaVent100 = forecast_item.get('probawind100', '')

        print(f'Pour {DateHeure}, la température prévue est {Temperature}°C. '
              f'Concernant le vent, le vent moyen sera de {VentMoyen}km/h avec une direction de {DirectionVent}° '
              f'et des rafales à {RafaleVent}km/h. '
              f'Le temps prévu est : {DescriptionMeteo}. '
              f'La probabilité de vent supérieur à 70km/h est de {ProbaVent70}% et la probabilité de vent supérieur à '
              f'100km/h est de {ProbaVent100}%.')

        # Ajoute les données extraites aux listes correspondantes.
        heures.append(DateHeure)
        vent_moyen.append(VentMoyen)
        rafale_vent.append(RafaleVent)
        temperature.append(Temperature)
        direction_vent.append(DirectionVent)
        prevision_meteo.append(DescriptionMeteo)

    # Appelle des fonctions de création de graphiques avec les données extraites.
    func_creation_graphique_temp_vent(heures, temperature, vent_moyen, rafale_vent, ZoneMeteo, PeriodeBulletin)
    func_creation_graphique_direction_vent_12h(heures, direction_vent, ZoneMeteo, PeriodeBulletin)
    func_creation_graphique_condition_meteo(heures, prevision_meteo, ZoneMeteo, PeriodeBulletin)

def func_decode_data_futures_14j(data, ZoneMeteo, PeriodeBulletin):
    """
    Fonction pour décoder et afficher les prévisions météorologiques pour les 14 prochains jours.
    :param data: Les données JSON en entrée.
    :param ZoneMeteo: La zone météorologique.
    :param PeriodeBulletin: La période du bulletin.
    :return: Aucune valeur de retour.
    """
    decoded_data = json.loads(json.dumps(data))  # Convertit les données JSON en un dictionnaire Python.

    print(f"Bulletin météo prévisionnel de {ZoneMeteo} pour les {PeriodeBulletin}.")

    # Dictionnaire de codes météorologiques pour les descriptions.
    WEATHER = {
        0: "Soleil",
        1: "Peu nuageux",
        2: "Ciel voilé",
        3: "Nuageux",
        4: "Très nuageux",
        5: "Couvert",
        6: "Brouillard",
        7: "Brouillard givrant",
        10: "Pluie faible",
        11: "Pluie modérée",
        12: "Pluie forte",
        13: "Pluie faible verglaçante",
        14: "Pluie modérée verglaçante",
        15: "Pluie forte verglaçante",
        16: "Bruine",
        20: "Neige faible",
        21: "Neige modérée",
        22: "Neige forte",
        30: "Pluie et neige mêlées faibles",
        31: "Pluie et neige mêlées modérées",
        32: "Pluie et neige mêlées fortes",
        40: "Averses de pluie locales et faibles",
        41: "Averses de pluie locales",
        42: "Averses locales et fortes",
        43: "Averses de pluie faibles",
        44: "Averses de pluie",
        45: "Averses de pluie fortes",
        46: "Averses de pluie faibles et fréquentes",
        47: "Averses de pluie fréquentes",
        48: "Averses de pluie fortes et fréquentes",
        60: "Averses de neige localisées et faibles",
        61: "Averses de neige localisées",
        62: "Averses de neige localisées et fortes",
        63: "Averses de neige faibles",
        64: "Averses de neige",
        65: "Averses de neige fortes",
        66: "Averses de neige faibles et fréquentes",
        67: "Averses de neige fréquentes",
        68: "Averses de neige fortes et fréquentes",
        70: "Averses de pluie et neige mêlées localisées et faibles",
        71: "Averses de pluie et neige mêlées localisées",
        72: "Averses de pluie et neige mêlées localisées et fortes",
        73: "Averses de pluie et neige mêlées faibles",
        74: "Averses de pluie et neige mêlées",
        75: "Averses de pluie et neige mêlées fortes",
        76: "Averses de pluie et neige mêlées faibles et nombreuses",
        77: "Averses de pluie et neige mêlées fréquentes",
        78: "Averses de pluie et neige mêlées fortes et fréquentes",
        100: "Orages faibles et locaux",
        101: "Orages locaux",
        102: "Orages fort et locaux",
        103: "Orages faibles",
        104: "Orages",
        105: "Orages forts",
        106: "Orages faibles et fréquents",
        107: "Orages fréquents",
        108: "Orages forts et fréquents",
        120: "Orages faibles et locaux de neige ou grésil",
        121: "Orages locaux de neige ou grésil",
        122: "Orages locaux de neige ou grésil",
        123: "Orages faibles de neige ou grésil",
        124: "Orages de neige ou grésil",
        125: "Orages de neige ou grésil",
        126: "Orages faibles et fréquents de neige ou grésil",
        127: "Orages fréquents de neige ou grésil",
        128: "Orages fréquents de neige ou grésil",
        130: "Orages faibles et locaux de pluie et neige mêlées ou grésil",
        131: "Orages locaux de pluie et neige mêlées ou grésil",
        132: "Orages fort et locaux de pluie et neige mêlées ou grésil",
        133: "Orages faibles de pluie et neige mêlées ou grésil",
        134: "Orages de pluie et neige mêlées ou grésil",
        135: "Orages forts de pluie et neige mêlées ou grésil",
        136: "Orages faibles et fréquents de pluie et neige mêlées ou grésil",
        137: "Orages fréquents de pluie et neige mêlées ou grésil",
        138: "Orages forts et fréquents de pluie et neige mêlées ou grésil",
        140: "Pluies orageuses",
        141: "Pluie et neige mêlées à caractère orageux",
        142: "Neige à caractère orageux",
        210: "Pluie faible intermittente",
        211: "Pluie modérée intermittente",
        212: "Pluie forte intermittente",
        220: "Neige faible intermittente",
        221: "Neige modérée intermittente",
        222: "Neige forte intermittente",
        230: "Pluie et neige mêlées",
        231: "Pluie et neige mêlées",
        232: "Pluie et neige mêlées",
        235: "Averses de grêle",
    }

    heures = []
    vent_moyen = []
    rafale_vent = []
    temperature = []
    direction_vent = []
    prevision_meteo = []

    for forecast_item in decoded_data.get("forecast", []):

        for item in forecast_item:
            # Récupération de la date et l'heure de la prévision
            DateHeureOriginal = item.get('datetime', '')

            date_part, heure_part = DateHeureOriginal.split('T')
            date_universelle = date_part
            heure_universelle = heure_part[:5]
            DateHeure = f"{date_universelle} {heure_universelle}"

            # Récupération de la température de la prévision
            Temperature = item.get('temp2m', '')

            # Récupération de la vitesse du vent moyen de la prévision
            VentMoyen = item.get('wind10m', '')

            # Récupération de la vitesse des rafales de vent de la prévision
            RafaleVent = item.get('gust10m', '')

            # Récupération de la direction du vent de la prévision
            DirectionVent = item.get('dirwind10m', '')

            # Récupération du code météo de la prévision
            CodeMeteo = item.get('weather', '')
            # Conversion du code météo en description détaillée
            DescriptionMeteo = WEATHER.get(CodeMeteo, 'Inconnu')

            # Récupération de la probabilité des vents au-dessus de 70km/h
            ProbaVent70 = item.get('probawind70', '')

            # Récupération de la probabilité des vents au-dessus de 100km/h
            ProbaVent100 = item.get('probawind100', '')

            print(f'Pour {DateHeure}, la température prévue est {Temperature}°C. '
                  f'Concernant le vent, le vent moyen sera de {VentMoyen}km/h avec une direction de {DirectionVent}° '
                  f'et des rafales à {RafaleVent}km/h. '
                  f'Le temps prévu est : {DescriptionMeteo}. '
                  f'La probabilité de vent supérieur à 70km/h est de {ProbaVent70}% et la probabilité de vent supérieur à '
                  f'100km/h est de {ProbaVent100}%.')

            # Ajoute les données extraites aux listes correspondantes.
            heures.append(DateHeure)
            vent_moyen.append(VentMoyen)
            rafale_vent.append(RafaleVent)
            temperature.append(Temperature)
            direction_vent.append(DirectionVent)
            prevision_meteo.append(DescriptionMeteo)

        # Appelle des fonctions de création de graphiques avec les données extraites.
        func_creation_graphique_temp_vent(heures, temperature, vent_moyen, rafale_vent, ZoneMeteo, PeriodeBulletin)
        func_creation_graphique_direction_vent_14j(heures, direction_vent, ZoneMeteo, PeriodeBulletin)
        func_creation_graphique_condition_meteo(heures, prevision_meteo, ZoneMeteo, PeriodeBulletin)