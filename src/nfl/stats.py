import requests
import json


def get_defenses(season, week):
    week = week - 1  # we need last weeks stats
    defenses = []
    url = "http://api.fantasy.nfl.com/v1/players/scoringleaders?"
    url += "season=" + str(season)
    url += "&week=" + str(week)
    url += "&position=DEF"
    url += "&format=json"
    r = requests.get(url)
    result = json.loads(r.text)
    for defense in result["positions"]["DEF"]:
        defenses.append(defense)
    return defenses


def get_qbs(season, week):
    week = week - 1  # we need last weeks stats
    qbs = []
    url = "http://api.fantasy.nfl.com/v1/players/scoringleaders?"
    url += "season=" + str(season)
    url += "&week=" + str(week)
    url += "&position=QB"
    url += "&format=json"
    r = requests.get(url)
    result = json.loads(r.text)
    for qb in result["positions"]["QB"]:
        qbs.append(qb["firstName"] + " " + qb["lastName"])
    return qbs


def get_rbs(season, week):
    week = week - 1  # we need last weeks stats
    rbs = []
    url = "http://api.fantasy.nfl.com/v1/players/scoringleaders?"
    url += "season=" + str(season)
    url += "&week=" + str(week)
    url += "&position=RB"
    url += "&format=json"
    r = requests.get(url)
    result = json.loads(r.text)
    for rb in result["positions"]["RB"]:
        rbs.append(rb["firstName"] + " " + rb["lastName"])
    return rbs


def get_tes(season, week):
    week = week - 1  # we need last weeks stats
    tes = []
    url = "http://api.fantasy.nfl.com/v1/players/scoringleaders?"
    url += "season=" + str(season)
    url += "&week=" + str(week)
    url += "&position=TE"
    url += "&format=json"
    r = requests.get(url)
    result = json.loads(r.text)
    for te in result["positions"]["TE"]:
        tes.append(te["firstName"] + " " + te["lastName"])
    return tes


def get_wrs(season, week):
    week = week - 1  # we need last weeks stats
    wrs = []
    url = "http://api.fantasy.nfl.com/v1/players/scoringleaders?"
    url += "season=" + str(season)
    url += "&week=" + str(week)
    url += "&position=WR"
    url += "&format=json"
    r = requests.get(url)
    result = json.loads(r.text)
    for wr in result["positions"]["WR"]:
        wrs.append(wr["firstName"] + " " + wr["lastName"])
    return wrs
