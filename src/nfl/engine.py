###############################################################################
# Engine
# This is the driving force behind the application. We first adjust all of the
# point values, then pass those updated players to the alogrithm of our
# choosing. You should be able to pop another adjuster or algorithm in without
# any trouble.
###############################################################################


import nfl.adjusters
import nfl.algorithms
import nfl.trimmers


###############################################################################
# Start
# Here is where we call all of the trimmers, adjusters, and algorithms needed
# to select our team.
###############################################################################
def start(season, week, players):
    print "Trimming players..."
    players = nfl.trimmers.default(players)

    # You can create new adjuster functions inside of nfl/adjusters
    print "Adjusting players..."
    players = nfl.adjusters.oprk(season, week, players)

    # You can create new algorithms inside nfl/algorithms and use them here
    print "Picking teams..."
    nfl.algorithms.default(players)
