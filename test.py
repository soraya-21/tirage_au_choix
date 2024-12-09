import json
import random

# Fonction pour charger le fichier JSON
with open("data/teams.json", "r") as file:
    teams = json.load(file)


# Fonction pour créer le format de tirage
def get_chapeau(teams):
    pot1, pot2, pot3, pot4 = [], [], [], []

    for team in teams:
        # On récupère le nom de l'équipe (clé) et ses informations
        team_name = team["nom"]  # Suppose que chaque dict a une clé 'name'
        # print(team_name)
        # Vérifier le champ "chapeau" dans les informations de l'équipe
        if team["chapeau"] == 1:
            pot1.append(
                {
                    "nom": team["nom"],
                    "pays": team["pays"],
                    "championnat": team["championnat"],
                    "chapeau": team["chapeau"],
                    "logo": team["logo"],
                }
            )
        elif team["chapeau"] == 2:
            pot2.append(
                {
                    "nom": team["nom"],
                    "pays": team["pays"],
                    "championnat": team["championnat"],
                    "chapeau": team["chapeau"],
                    "logo": team["logo"],
                }
            )
        elif team["chapeau"] == 3:
            pot3.append(
                {
                    "nom": team["nom"],
                    "pays": team["pays"],
                    "championnat": team["championnat"],
                    "chapeau": team["chapeau"],
                    "logo": team["logo"],
                }
            )
        else:
            pot4.append(
                {
                    "nom": team["nom"],
                    "pays": team["pays"],
                    "championnat": team["championnat"],
                    "chapeau": team["chapeau"],
                    "logo": team["logo"],
                }
            )

    home = random.choice(pot1)
    away = random.choice(pot1)

    # while home == away:
    #     away = random.choice(pot1)
    # print(f"Pot 1: {home} vs {away}")

    return [
        home,
        away,
    ]


def creer_format_tirage(teams):
    result = {}
    pots = get_chapeau(teams)
    print("POTS", pots)
    #     # Itération sur les équipes dans ce pot
    #     # Boucler sur chaque pot et ensuite equipe pour créer le tirage
    for equipe in teams:
        print(equipe["nom"])
        result[equipe["nom"]] = {
            "ville": equipe["nom"].split()[
                0
            ],  # Ville fictive basée sur le premier mot du nom
            "pays": equipe["pays"],
            "championnat": equipe["championnat"],
            "chapeau": equipe["chapeau"],
            "logo": equipe["logo"],
            "pot_1": {
                "home": pots[0],  # Vérifier si assez d'équipes dans pot 2
                "away": pots[1],
            },
            "pot_2": {
                "home": pots[0],  # Vérifier si assez d'équipes dans pot 2
                "away": pots[1],
            },
            "pot_3": {
                "home": pots[0],  # Vérifier si assez d'équipes dans pot 3
                "away": pots[1],
            },
            "pot_4": {
                "home": pots[0],  # Vérifier si assez d'équipes dans pot 4
                "away": pots[1],
            },
        }
    return result


# Fonction pour exporter le résultat au format JSON
def exporter_resultat(filepath, data):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# Repartition des equipes par chapeau
chapeaux = get_chapeau(teams)
print("CHAPEAU", chapeaux)
# Créer le tirage
tirage = creer_format_tirage(teams)
# Exporter le résultat dans un fichier JSON
exporter_resultat("resultat_tirage.json", tirage)

print("Le tirage a été effectué et sauvegardé dans 'resultat_tirage.json'.")
