class Team:
    def __init__(self, team):
        self.team = team

    def display(self):
        print "\n"
        print "{0:10} {1:20} {2:7} {3:10}".format("Pos", "Name", "Salary",
                                                  "Points")
        for player in self.team:
            print "{0:10} {1:20} {2:7} {3:10}".format(player["position"],
                                                      player["name"],
                                                      player["salary"],
                                                      player["avg_points"])
        print "Total Salary: " + str(self.get_salary())
        print "Expected Points: " + str(self.get_value())

    def get_salary(self):
        total_salary = 0
        for player in self.team:
            total_salary += int(player["salary"])
        return total_salary

    def get_value(self):
        total_value = 0
        for player in self.team:
            total_value += float(player["avg_points"])
        return total_value

    def has_positions(self):
        positions = []
        for player in self.team:
            positions.append(player["position"])

        try:
            positions.remove("QB")
            positions.remove("RB")
            positions.remove("RB")
            positions.remove("WR")
            positions.remove("WR")
            positions.remove("WR")
            positions.remove("RB")
            positions.remove("TE")
            positions.remove("DST")
        except ValueError:
            return False

        if len(positions) == 0:
            return True
        else:
            return False
