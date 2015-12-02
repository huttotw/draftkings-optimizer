###############################################################################
# Algorithms
# The algorithm should take the adjusted values from the adjuster and compare
# them to see if the current team is better than the last. You should not
# modify any values or look up an additional statistics here, it is mearly a
# comparison function.
###############################################################################


import itertools
import math
import sys
from nfl.team import Team


###############################################################################
# nCr
# Function for computing the number of combinations, note permutations are
# different and not needed for this application.
###############################################################################
def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


###############################################################################
# Default
# We adjust the players average based on their opponent's defensive ranking.
###############################################################################
def default(players):
    max_value = 0  # Define our max value starting point.
    numOfCombinations = nCr(len(players), 9)  # Figure out how many teams

    for i, combo in enumerate(itertools.combinations(players, 9)):
        #  Display our progress to the screen
        progress = "\r[{0}/{1}]".format(i, numOfCombinations)
        sys.stdout.write(progress)
        sys.stdout.flush()

        # Create the team
        team = Team(combo)

        # Decide if this team is good or not
        if team.has_positions() and team.get_salary() <= 50000:
            team_value = team.get_value()
            if team_value >= max_value:
                max_value = team_value
                team.display()
