# Ce module contient la classe de tirage au sort.


class Draw:
    def __init__(self, teams: [dict]) -> None:
        # Définissez les attributs dont vous aurez besoin
        self.teams = teams

    # Définissez les méthodes dont vous aurez besoin
    def premier_equipe(self):
        new_teams = []
        # Cette méthode permettra de faire un premier tirage au sort.
        # Prendre la premiere equipe
        new_teams.append(self.teams[0])

        print("Premier tirage au sort effectué")

        tirage = {}
        new_teams.append(tirage)

    def get_chapeau(self):
        pot1, pot2, pot3, pot4 = [], [], [], []

        for team, info in self.teams.items():
            # On récupère le nom de l'équipe (clé) et ses informations
            team_name = info["chapeau"]  # Suppose que chaque dict a une clé 'name'

            # Vérifier le champ "chapeau" dans les informations de l'équipe
            if info["chapeau"] == "pot_1":
                pot1.append(team_name)
            elif info["chapeau"] == "pot_2":
                pot2.append(team_name)
            elif info["chapeau"] == "pot_3":
                pot3.append(team_name)
            else:
                pot4.append(team_name)

        return pot1, pot2, pot3, pot4

    def make_draw(self):
        # Cette méthode sera celle appelée pour effectuer votre tirage au sort.
        print("Tirage au sort effectué")
