import os
from Traitement_data import func_decode_data_actuelles_json
from Traitement_data import func_decode_data_futures_12h
from Traitement_data import func_decode_data_futures_14j
from Request_api import func_requete_api
from Traitement_Config import func_import_config

RepertoireConfiguration = 'C:\\Projets_Python\\01_Projets_en_cours\\Meteo_France'
CheminConfig = os.path.join(RepertoireConfiguration, "Configuration.json")

# Récupération token de connexion
api_key = func_import_config(CheminConfig, 'API_Key')

# Récupération liste zones météo à traiter
Liste_Meteo = func_import_config(CheminConfig, 'Configuration')

# Traitement pour chaque zone météo à Traiter
for Element_Liste_Meteo in Liste_Meteo:
    Nom_Zone_Meteo = Element_Liste_Meteo['Nom_Zone_Meteo']
    latitude = Element_Liste_Meteo['Latitude']
    longitude = Element_Liste_Meteo['Longitude']
    rayon = Element_Liste_Meteo['Rayon_Data_Km']


    # Effectuez la requête à l'API Meteo-Concept pour avoir la météo actuelle
    url = f'https://api.meteo-concept.com/api/observations/around?token={api_key}&latlng={latitude},{longitude}&radius={rayon}'

    data_actuelles = func_requete_api(url)

    func_decode_data_actuelles_json(data_actuelles)

     # Requete à l'API Météo-Concept pour avoir la météo pour les 12 prochaines heures
    url2 = f'https://api.meteo-concept.com/api/forecast/nextHours?token={api_key}&latlng={latitude},{longitude}&hourly=true&world=false'

    data_futures_12h = func_requete_api(url2)
    NomPeriode12h = "12 prochaines heures"
    func_decode_data_futures_12h(data_futures_12h, Nom_Zone_Meteo, NomPeriode12h)

     # Requete à l'API Météo-Concept pour avoir la météo pour les 14 prochains jours
    url3 = f'https://api.meteo-concept.com/api/forecast/daily/periods?token={api_key}&latlng={latitude},{longitude}&world=false'

    data_futures_14j = func_requete_api(url3)
    NomPeriode14j = "14 prochains jours"
    func_decode_data_futures_14j(data_futures_14j, Nom_Zone_Meteo, NomPeriode14j)