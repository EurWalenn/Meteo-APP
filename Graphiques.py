import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def func_creation_graphique_temp_vent(heures, temperatures, vitesses_vent, rafales_vent, Zone_Meteo, PeriodeBulletin):
    """
    Crée un graphique de la température et de la vitesse du vent en fonction des heures.
    :param heures: Liste des heures.
    :param temperatures: Liste des températures en °C.
    :param vitesses_vent: Liste des vitesses du vent en km/h.
    :param rafales_vent: Liste des rafales du vent en km/h.
    :param Zone_Meteo: Zone météorologique.
    :param PeriodeBulletin: Période du bulletin météo.
    :return: None
    """

    # Création graphique
    fig, ax1 = plt.subplots(figsize=(12, 6))  # Création d'une figure et un premier axe

    # Ajoutez la température sur le premier axe Y
    ax1.plot(heures, temperatures, label='Température (°C)', marker='o', color='red')
    ax1.set_xlabel('Heures')
    ax1.set_ylabel('Température (°C)', color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    # Définissez les étiquettes d'axe x sur l'axe principal (ax1)
    ax1.set_xticks(heures)
    ax1.set_xticklabels(heures, rotation=45, ha='right')  # Rotation des étiquettes

    # Créez un deuxième axe Y partageant le même axe des x
    ax2 = ax1.twinx()

    # Ajoutez la vitesse du vent et les rafales sur le deuxième axe Y
    ax2.plot(heures, vitesses_vent, label='Vitesse du vent (km/h)', marker='s', color='blue')
    ax2.plot(heures, rafales_vent, label='Rafales de vent (km/h)', marker='^', color='green')
    ax2.set_ylabel('Vitesse du vent (km/h)', color='black')
    ax2.tick_params(axis='y', labelcolor='black')

    # Réglage des étiquettes d'axe et le titre
    plt.xlabel('Heures')
    plt.ylabel('Vitesse Vent (km/h)')
    plt.title(f'Prévision de Température, Vitesse du Vent et Rafales de Vent pour les {PeriodeBulletin} à {Zone_Meteo}')

    # Ajout de la légende
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper right')

    # Affichage du graphique
    plt.grid(True)  # Affichez une grille
    plt.tight_layout()  # Ajustement automatique de la mise en page

    # Sauvegardez le graphique dans un fichier (facultatif)
    plt.savefig(f'{Zone_Meteo}_{PeriodeBulletin}_Temp_Vent.png')
    plt.close()

def func_creation_graphique_direction_vent_12h(heures, directions_vent_degrees, Zone_Meteo, PeriodeBulletin):
    """
    Crée un graphique en forme de rosace pour afficher la direction du vent sur 12 heures.

    :param heures: Liste des heures.
    :param directions_vent_degrees: Liste des directions du vent en degrés.
    :param Zone_Meteo: Zone météorologique.
    :param PeriodeBulletin: Période du bulletin météo.
    :return: None
    """

    # Conversion des directions du vent en radians
    directions_radians = np.deg2rad(directions_vent_degrees)

    # Couleurs pour chaque heure
    couleurs = plt.cm.jet(np.linspace(0, 1, len(heures)))

    # Création d'un graphique en forme de rosace
    fig = plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    # Plot des données pour chaque heure
    for i, heure in enumerate(heures):
        ax.plot(directions_radians[i], 1, marker='o', markersize=10, color=couleurs[i], label=heure)

    # Retirer les labels qui vont de 0 à 1 depuis le centre
    ax.set_yticklabels([])

    # Réglage du titre
    plt.title(f'Prévision de Direction du Vent pour les {PeriodeBulletin} à {Zone_Meteo}')

    # Ajout de la légende
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0), fontsize=8)

    # Personnalisation des étiquettes d'axe
    ax.set_xticks(np.linspace(0, 2 * np.pi, 16, endpoint=False))
    ax.set_xticklabels(
        ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW', 'WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE'])

    # Affichage du graphique
    plt.tight_layout()
    plt.savefig(f'{Zone_Meteo}_{PeriodeBulletin}_direction_vent.png')
    plt.close()

def func_creation_graphique_condition_meteo(heures, conditions_meteo, Zone_Meteo, PeriodeBulletin):
    """
    Crée un tableau HTML pour afficher les conditions météorologiques.

    :param heures: Liste des heures.
    :param conditions_meteo: Liste des conditions météorologiques.
    :param Zone_Meteo: Zone météorologique.
    :param PeriodeBulletin: Période du bulletin météo.
    :return: None
    """

    # Création d'un DataFrame à partir des données
    data = {'Heures': heures, 'Conditions Météo': conditions_meteo}
    df = pd.DataFrame(data)

    # Appliquer des styles au DataFrame pour le tableau HTML
    styles = [
        {"selector": "",
         "props": [("font-size", "16px"), ("text-align", "center")]},
        {"selector": "th",
         "props": [("font-size", "18px"), ("background-color", "#f2f2f2")]},
        {"selector": "tr:nth-child(even)",
         "props": [("background-color", "#f5f5f5")]},
        {"selector": "tr:nth-child(odd)",
         "props": [("background-color", "#ffffff")]}
    ]
    styled_df = df.style.set_table_styles(styles)

    # Générer le tableau HTML
    html_table = styled_df.to_html(escape=False, index=False)

    # Écrire le tableau HTML dans un fichier
    with open(f"{Zone_Meteo}_tableau_conditions_meteo_{PeriodeBulletin}.html", "w") as f:
        f.write(html_table)

def func_creation_graphique_direction_vent_14j(heures, directions_vent_degrees, Zone_Meteo, PeriodeBulletin):
    """
    Crée un graphique en forme de rosace pour afficher la direction du vent sur 14 jours.

    :param heures: Liste des heures.
    :param directions_vent_degrees: Liste des directions du vent en degrés.
    :param Zone_Meteo: Zone météorologique.
    :param PeriodeBulletin: Période du bulletin météo.
    :return: None
    """

    # Conversion des directions du vent en radians
    directions_radians = np.deg2rad(directions_vent_degrees)

    # Extraction des dates à partir des heures
    dates = [heure.split()[0] for heure in heures]

    # Création d'un dictionnaire pour regrouper les données par date
    data_par_date = {}
    for i, date in enumerate(dates):
        if date not in data_par_date:
            data_par_date[date] = {'directions': [], 'couleur': None}
        data_par_date[date]['directions'].append(directions_radians[i])

    # Couleurs pour chaque date
    couleurs = plt.cm.jet(np.linspace(0, 1, len(data_par_date)))

    # Création d'un graphique en forme de rosace
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # Plot des données pour chaque date
    for i, (date, data) in enumerate(data_par_date.items()):
        directions = data['directions']
        couleur = couleurs[i]
        ax.plot(directions, np.ones(len(directions)), marker='o', markersize=10, color=couleur, label=date,
                linestyle='None')  # linestyle='None' pour retirer les lignes

    # Retirer les labels qui vont de 0 à 1 depuis le centre
    ax.set_yticklabels([])

    # Réglage du titre
    plt.title(f'Prévision de Direction du Vent pour {Zone_Meteo} - {PeriodeBulletin}', fontsize=16)

    # Ajout de la légende
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0), title='Dates', fontsize=8)

    # Personnalisation des étiquettes d'axe
    ax.set_xticks(np.linspace(0, 2 * np.pi, 16, endpoint=False))
    ax.set_xticklabels(
        ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW', 'WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE'])

    # Ajuster les paramètres de la disposition pour éviter la coupure de la légende
    plt.subplots_adjust(right=0.8)

    # Affichage du graphique
    plt.tight_layout()
    plt.savefig(f'{Zone_Meteo}_{PeriodeBulletin}_direction_vent.png')
    plt.close()