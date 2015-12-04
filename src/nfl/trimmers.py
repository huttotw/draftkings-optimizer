###############################################################################
# Trimmers
# Trimmers are made to shorten the input, this is incredibly important. The
# fewer the players, the better chance we have of the algorithm completing and
# outputing the best team. I have found that on my computer, a roster of 36
# players completes in reasonable time ~ 15 minutes. Any roster length greater
# than 36 and you can expect a serious increase in compleation time.
#
# For more information on this type of program, see
# https://en.wikipedia.org/wiki/Knapsack_problem
###############################################################################


###############################################################################
# Default
# We don't trim any players from the input, every player from the input is
# included and sent to the adjuster.
###############################################################################
def top_n(players, n):
    # First sort by points
    players.sort(key=lambda x: x.get_points(), reverse=True)

    qbs = []
    rbs = []
    wrs = []
    tes = []
    dsts = []

    for player in players:
        if player.get_position() == "QB" and len(qbs) < n:
            qbs.append(player)

        if player.get_position() == "RB" and len(rbs) < n:
            rbs.append(player)

        if player.get_position() == "WR" and len(wrs) < n:
            wrs.append(player)

        if player.get_position() == "TE" and len(tes) < n:
            tes.append(player)

        if player.get_position() == "DST" and len(dsts) < n:
            dsts.append(player)

    return qbs + rbs + wrs + tes + dsts
