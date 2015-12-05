###############################################################################
# Engine
# This is the driving force behind the application. We first adjust all of the
# point values, then pass those updated players to the alogrithm of our
# choosing. You should be able to pop another adjuster or algorithm in without
# any trouble.
###############################################################################


import nfl.adjusters
import nfl.algorithms
import nfl.sanitizers
import nfl.trimmers


###############################################################################
# Start
# Here is where we call all of the trimmers, adjusters, and algorithms needed
# to select our team.
###############################################################################
def start(season, week, players):
    # You can create new santiziing functions inside of nfl/trimmers
    print "Sanitizing players..."
    players = nfl.sanitizers.default(players)

    # You can create new adjuster functions inside of nfl/adjusters
    print "Adjusting players..."
    players = nfl.adjusters.oprk_by_position(season, week, players)

    # You can create new trimmer functions inside of nfl/trimmers
    print "Trimming players..."
    players = nfl.trimmers.top_n_at_position(players, 6)

    # You can create new algorithms inside nfl/algorithms and use them here
    print "Running algorithm..."
    nfl.algorithms.default(players)
