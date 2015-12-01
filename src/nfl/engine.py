import nfl.adjusters
import nfl.algorithms


def start(season, week, players):
    # First we adjust the averages to make them more informational
    print "Adjusting players..."
    players = nfl.adjusters.oprk(season, week, players)

    print "Picking teams..."
    nfl.algorithms.default(players)
