###############################################################################
# Adjusters
# The goal here is to adjust the raw input by calculating outside factors.
# These outside factors could be runs, carries, touches, last performance.
# All of these statistics can be retreived from nfl.stats
# The more accurate the adjuster, the better chance you can produce a winning
# team.
###############################################################################

import nfl.stats


###############################################################################
# Default
# Purely based on Draft Kings rankings.
###############################################################################
def default(season, week, players):
    return players


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
        opponent = player.get_opponent()
        opponent_rank = defense_team_abbrs.index(opponent)
        coefficient = float(opponent_rank) / float(len(defenses))
        adjusted_value = coefficient * float(player.get_points())
        player.set_points(adjusted_value)

    return players


###############################################################################
# OPRK By Position
# Compare every player based on how
###############################################################################
def oprk_by_position(season, week, players):
    defenses = nfl.stats.get_leaders(season, week, "DEF")

    for player in players:
        for defense in defenses:
            if player.get_opponent() == defense["teamAbbr"]:

                # compile all the stats
                sacks = float(defense["stats"]["Sack"]) if defense["stats"]["Sack"] is not False else 1.0
                interceptions = float(defense["stats"]["Int"]) if defense["stats"]["Int"] is not False else 1.0
                fumble_recoveries = float(defense["stats"]["FumRec"]) if defense["stats"]["FumRec"] is not False else 1.0
                safeties = float(defense["stats"]["Saf"]) if defense["stats"]["Saf"] is not False else 1.0
                touchdowns = float(defense["stats"]["TD"]) if defense["stats"]["TD"] is not False else 1.0
                return_touchdowns = float(defense["stats"]["RetTD"]) if defense["stats"]["RetTD"] is not False else 1.0
                points_allowed = float(defense["stats"]["PtsAllowed"]) if defense["stats"]["PtsAllowed"] is not False else 1.0
                fantasy_points = float(defense["pts"]) if defense["pts"] is not False else 1.0
                fantasy_projected_points = float(defense["projectedPts"]) if defense["projectedPts"] is not False else 1.0

                player_value = player.get_points()

                if player.get_position() == "QB":
                    # decrease values for things that will hurt qb
                    player_value = player_value / sacks
                    player_value = player_value / interceptions

                    # increase values for things that will help qb
                    player_value = player_value * points_allowed / 2

                if player.get_position() == "RB":
                    # decrease values for things that will hurt rb
                    player_value = player_value / fumble_recoveries

                    # increase values for things that will help rb
                    player_value = player_value * points_allowed / 2

                if player.get_position() == "WR" or player.get_position() == "TE":
                    # decrease values for things that will hurt rb
                    player_value = player_value / fumble_recoveries

                    # increase values for things that will help rb
                    player_value = player_value * points_allowed / 2

                if player.get_position() == "DEF":
                    # We can't tell anything from the opposing defense
                    player_value = player_value

                # update player
                player.set_points(player_value)

    return players
