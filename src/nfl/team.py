###############################################################################
# Team
# A object representation of a Team of Players.
###############################################################################


class Team:
    def __init__(self, team):
        self.team = team

    def display(self):
        print "\n"
        print "{0:>5} {1:5} {2:25} {3:>10} {4:>15}".format("ID", "Pos", "Name",
                                                           "Salary", "Points")
        for player in self.team:
            player.display()
        print "Total Salary: " + str(self.get_salary())
        print "Expected Points: " + str(self.get_value())

    def get_salary(self):
        total_salary = 0
        for player in self.team:
            total_salary += int(player.get_salary())
        return total_salary

    def get_value(self):
        total_value = 0
        for player in self.team:
            total_value += float(player.get_points())
        return total_value

    def is_valid(self):
        return len(self.team) is len(set(self.team))

    def has_positions(self):
        positions = []
        for player in self.team:
            positions.append(player.get_position())

        # Use the list as a stack, popping positions and expecting len = 0
        try:
            positions.remove("QB")
            positions.remove("RB")
            positions.remove("RB")
            positions.remove("WR")
            positions.remove("WR")
            positions.remove("WR")
            positions.remove("TE")
            positions.remove("DST")
        except ValueError:
            return False

        if len(positions) == 0:
            return True
        else:
            return False
