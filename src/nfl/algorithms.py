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
import numpy as np


def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = n / arrays[0].size
    out[:, 0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m, 1:])
        for j in xrange(1, arrays[0].size):
            out[j*m:(j+1)*m, 1:] = out[0:m, 1:]
    return out


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
def brute_force(players):
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


def default(players):
    max_value = 0  # Define our max value starting point.
    numOfCombinations = nCr(len(players), 9)  # Figure out how many teams

    qbs = []
    rbs = []
    wrs = []
    tes = []
    defs = []
    for player in players:
        if player.get_position() == "QB":
            qbs.append(player)
        elif player.get_position() == "RB":
            rbs.append(player)
        elif player.get_position() == "WR":
            wrs.append(player)
        elif player.get_position() == "TE":
            tes.append(player)
        elif player.get_position() == "DST":
            defs.append(player)

    print "Calculating cartesian product..."
    teams = cartesian((qbs, rbs, rbs, wrs, wrs, wrs, tes, defs))

    print "Looking for best team..."
    for team in teams:
        team = Team(combo)

        # Decide if this team is good or not
        if team.has_positions() and team.get_salary() <= 50000:
            team_value = team.get_value()
            if team_value >= max_value:
                max_value = team_value
                team.display()
