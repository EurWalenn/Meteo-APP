import json

#Liste des fonctions liées à la configuration

def func_import_config(CheminFichierConfig, ItemConfig):
    """
    Fonction de gestion du fichier de configuration et chargement des informations
    :param CheminFichierConfig: Chemin du fichier de configuration
            ItemConfig : Element dans la configuration à récupérer
    :return: La liste des éléments nécéssaires à la gestion de l'application
    """
    try:
        with open(CheminFichierConfig, 'r') as f:
            ConfigFile = json.load(f)[ItemConfig]
        return ConfigFile

    except FileNotFoundError:
        message = f"Le fichier de configuration '{ConfigFile}' n'a pas été trouvé."
        print(message)

    except KeyError:
        message = f"L'élément {ItemConfig} n'a pas été trouvé dans le fichier '{ConfigFile}'."
        print(message)

    except json.JSONDecodeError:
        message = f"Erreur lors de la lecture du fichier de configuration JSON '{ConfigFile}'."
        print(message)