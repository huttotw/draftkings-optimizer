###############################################################################
# Adjusters
# The goal here is to adjust the raw input by calculating outside factors.
# These outside factors could be runs, carries, touches, last performance.
# All of these statistics can be retreived from nfl.stats
# The more accurate the adjuster, the better chance you can produce a winning
# team.
###############################################################################

import nfl.stats
import re


###############################################################################
# OPRK
# We adjust the players average based on their opponent's defensive ranking.
###############################################################################
def oprk(season, week, players):
    defenses = nfl.stats.get_leaders(season, week, "DEF")
    defense_team_abbrs = []
    for defense in defenses:
        defense_team_abbrs.append(defense["teamAbbr"])

    for player in players:
        game = player.get_game()
        teams = re.search("^(\S+)@(\S+)\s", game)  # separate into 2 teams
        team1 = teams.group(1)  # get the first team
        team2 = teams.group(2)  # get the second team

        # get the opponent
        if team1 == player.get_team():
            opponent = team2
        else:
            opponent = team1

        opponent_rank = defense_team_abbrs.index(opponent)
        coefficient = float(opponent_rank) / float(len(defenses))
        adjusted_value = coefficient * float(player.get_points())
        player.set_points(adjusted_value)

    return players
