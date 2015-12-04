###############################################################################
# Player
# A object representation of an NFL player.
###############################################################################


class Player:

    def __init__(self, position, name, salary, game, points, team):
        self.position = position.upper()
        self.name = name.upper()
        self.salary = int(salary)
        self.game = game.upper()
        self.points = float(points)
        self.team = team.upper()

    def display(self):
        print "{0:10} {1:20} {2:10} {3:10}".format(self.position,
                                                  self.name,
                                                  self.salary,
                                                  self.points)

    def get_opponent(self):
        teams = re.search("^(\S+)@(\S+)\s", self.game)  # separate into 2 teams
        team1 = teams.group(1)  # get the first team
        team2 = teams.group(2)  # get the second team

        # get the opponent
        if team1 == player.get_team():
            opponent = team2
        else:
            opponent = team1
        return opponent

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def get_game(self):
        return self.game

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def get_team(self):
        return self.team
