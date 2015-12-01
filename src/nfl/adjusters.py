import nfl.stats
import re


###############################################################################
# OPRK
# We adjust the players average based on their opponent's defensive ranking.
###############################################################################
def oprk(season, week, players):
    defenses = nfl.stats.get_defenses(season, week)
    defense_team_abbrs = []
    for defense in defenses:
        defense_team_abbrs.append(defense["teamAbbr"])

    for player in players:
        game = player["game"]
        teams = re.search("^(\S+)@(\S+)\s", game)  # separate into 2 teams
        team1 = teams.group(1)  # get the first team
        team2 = teams.group(2)  # get the second team

        # get the opponent
        if team1 == player["team_abbr"]:
            opponent = team2
        else:
            opponent = team1

        opponent_rank = defense_team_abbrs.index(opponent)
        coefficient = float(opponent_rank) / float(len(defenses))
        adjusted_value = coefficient * float(player["avg_points"])
        player["avg_points"] = adjusted_value

    return players
