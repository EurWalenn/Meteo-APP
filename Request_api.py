import requests

def func_requete_api(url):
    """
    Effectue une requête HTTP GET vers l'URL spécifiée et affiche les résultats en fonction du code de statut.
    :param url: L'URL de l'API à interroger.
    :return: Les données de la réponse JSON si la requête réussit.
    """

    print(url)  # Affiche l'URL de la requête

    response = requests.get(url)

    # Vérifiez si la requête a réussi
    if response.status_code == 200:
        print("200 : Connexion OK.")
        data = response.json()  # Convertit la réponse en JSON
        return data  # Renvoie les données JSON si la requête a réussi
    elif response.status_code == 400:
        print("400 : Paramètre manquant, ou valeur incorrecte. Vérifiez également si le quota n'est pas dépassé.")
    elif response.status_code == 401:
        print("401 : Authentification nécessaire (token absent ou invalide).")
    elif response.status_code == 403:
        print("403 : Action non autorisée (URL non autorisée avec votre abonnement).")
    elif response.status_code == 404:
        print("404 : Page inaccessible (URL inconnue).")
    elif response.status_code == 500:
        print("500: Erreur interne au serveur, contactez-nous.")
    elif response.status_code == 503:
        print("503 : L'API est momentanément indisponible, réessayez dans quelques minutes.")