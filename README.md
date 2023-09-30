# Meteo-APP - Application de Récupération de Données météo depuis api.meteo-concept.com

## Description:
Ce dépôt contient une application conçue pour récupérer des données météo auprès de api.meteo-concept.com en utilisant son API (https://api.meteo-concept.com/).
L'application se concentre surtout sur les données françaises.

L'application récupère des données météorologiques via l'API api.meteo-concept.com en fonction de paramètres de configuration spécifiés dans un fichier de configuration JSON.

## Fonctionnalités:
Récupération de données météorologiques.
Configuration des paramètres d'acquisition via un fichier de configuration JSON.
Génération de requêtes API pour récupérer les données.
Création de figures de données à partir des résultats obtenus.

## Structure du Code:
Le code est divisé en plusieurs modules pour améliorer la lisibilité et la maintenance. Voici un aperçu de chaque module :

Meteo_App.py : Point d'entrée de l'application, orchestre les étapes de récupération et de traitement des données.
Traitement_Config.py : Gère l'importation des paramètres de configuration depuis un fichier JSON.
Traitement_data.py : Gère le traitement des données JSON provenant de l'API avant de lancer les traitements pour l'affichage des graphiques.
Graphiques.py : Permet la création des différents graphiques et tableaux de données après traitement des données provenant de l'API.
Request_api.py : Permet de tester la connexion avec l'API, récupérer les données ou indiquer les problèmes de connexion si besoin.


## Utilisation:
Clonez ce dépôt sur votre machine locale.
Configurez les paramètres d'acquisition dans le fichier Configuration.json et mettez à jour 'RepertoireConfiguration' dans le script Meteo_App.py avec un chemin valide.
Exécutez le script Meteo_App.py pour lancer le traitement.
Les données récupérées seront enregistrées dans le répertoire ou se trouve Meteo_App.py

## Fichier de configuration :
Modifiez l'API_Key dans le fichier de configuration Configuration.json avec celle que vous avez obtenue sur https://api.meteo-concept.com
Nom_Zone_Meteo est le nom du lieu que vous souhaitez atteindre.
Latitude et Longitude sont les coordonnées du points ou vous souhaitez obtenir les informations météo.
Rayon_Data_Km est la distance a considérer pour obtenir une station météo. Si l'application ne tourne pas, il est possible que cela vienne du fait que le Rayon_Data_KM est trop faible.

## Contributions:
Les contributions sont les bienvenues ! Si vous souhaitez apporter des améliorations ou corriger des problèmes, n'hésitez pas à créer une demande de pull.

## Exemples de fichiers de sortie :
Vous pouvez voir les exemples dans le répertoire Exemples_Resultats.

## Avertissement:
Veuillez noter que l'utilisation de cette application est soumise aux conditions d'utilisation de https://api.meteo-concept.com/documentation. Assurez-vous de respecter les règles d'utilisation avant de lancer le traitement et inscrivez vous sur le site pour récupérer votre token.
