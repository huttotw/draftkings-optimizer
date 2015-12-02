###############################################################################
# Stats
# This modules makes use of NFL.com to retrieve the latest information on
# players and defenses. You should be able to creatively use this information
# to develop better and more complex adjusters.
#
# For complete documenation, see:
# http://api.fantasy.nfl.com/v1/docs
###############################################################################


import requests
import json


def get(season, week, position):
    week = week - 1  # we need last weeks stats
    results = []
    url = "http://api.fantasy.nfl.com/v1/players/scoringleaders?"
    url += "season=" + str(season)
    url += "&week=" + str(week)
    url += "&position=" + str(position)
    url += "&format=json"
    r = requests.get(url)
    result = json.loads(r.text)
    for result in result["positions"][str(position)]:
        results.append(result)
    return results
