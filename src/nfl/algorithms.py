import itertools
import math
import sys
from nfl.team import Team


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def default(players):
    max_value = 0
    numOfCombinations = nCr(len(players), 9)

    for i, combo in enumerate(itertools.combinations(players, 9)):
        #  Display our progress to the screen
        progress = "\r[{0}/{1}]".format(i, numOfCombinations)
        sys.stdout.write(progress)
        sys.stdout.flush()

        team = Team(combo)

        if team.has_positions() and team.get_salary() <= 50000:
            team_value = team.get_value()
            if team_value >= max_value:
                max_value = team_value
                team.display()
