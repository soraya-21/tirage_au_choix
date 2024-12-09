# Ce module contient les instances de vos classes back et front end.
from draw import Draw
import json

with open("./data/teams.json", "r") as file:
    teams = json.load(file)
for team in teams:

    def convert_team_to_draw_format(team):
        # Structure de base
        team_info = {
            team["nom"]: {
                "pays": team["pays"],
                "championnat": team["championnat"],
                "chapeau": team["chapeau"],
                "logo": team["logo"],
                "tirage": {
                    "pot_1": {
                        "home": {
                            "nom": "PSG",
                            "pays": "France",
                            "championnat": "Ligue 1",
                            "chapeau": 1,
                            "logo": "Paris_Saint-Germain.png",
                        },
                        "away": {
                            "nom": "FC Barcelone",
                            "pays": "Espagne",
                            "championnat": "La Liga",
                            "chapeau": 1,
                            "logo": "Logo_FC_Barcelona.png",
                        },
                    },
                    "pot_2": {
                        "home": {
                            "nom": "Club Bruges",
                            "pays": "Belgique",
                            "championnat": "Jupiler Pro League",
                            "chapeau": 2,
                            "logo": "Club_Brugge.png",
                        },
                        "away": {
                            "nom": "Juventus Turin",
                            "pays": "Italie",
                            "championnat": "Serie A",
                            "chapeau": 2,
                            "logo": "Juventus_FC.png",
                        },
                    },
                    "pot_3": {
                        "home": {
                            "nom": "Celtic",
                            "pays": "Écosse",
                            "championnat": "Scottish Premiership",
                            "chapeau": 3,
                            "logo": "Celtic_fc.png",
                        },
                        "away": {
                            "nom": "PSV Eindhoven",
                            "pays": "Pays-Bas",
                            "championnat": "Eredivisie",
                            "chapeau": 3,
                            "logo": "psv_eindhoven.png",
                        },
                    },
                    "pot_4": {
                        "home": {
                            "nom": "Sturm Graz",
                            "pays": "Autriche",
                            "championnat": "Bundesliga Autrichienne",
                            "chapeau": 4,
                            "logo": "SK_Sturm_Graz.png",
                        },
                        "away": {
                            "nom": "Slovan Bratislava",
                            "pays": "Slovaquie",
                            "championnat": "Fortuna Liga",
                            "chapeau": 4,
                            "logo": "Slovan_Bratislava.png",
                        },
                    },
                },
            }
        }
        return team_info


# Convertir toutes les équipes dans le format désiré
formatted_teams = {}
newTeams = {}
for team in teams:
    formatted_teams.update(convert_team_to_draw_format(team))

# Affichage en format JSON
print(json.dumps(formatted_teams, indent=4, ensure_ascii=False))
teams.append(newTeams)
# with open('data.json',"w") as f:
#     json.dump(teams, f,ensure_ascii=false, indent=4)
# convert to new format json

print(teams)

# Création de votre instance de classe Draw
draw = Draw(formatted_teams)
draw.make_draw()
draw.get_chapeau()
