###############################################################################
# Sanitizers
# This module gets the input shaped the way you need it to perform the rest
# of your operations on it.
###############################################################################


def default(players):
    for i, player in enumerate(players):
        player.set_index(i)
    return players
