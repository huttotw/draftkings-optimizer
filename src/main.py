import csv
import nfl.engine


def parse_players(file_name):
    players = []
    with open(file_name, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            players.append({"position": row[0].upper(),
                            "name": row[1].upper(),
                            "salary": row[2].upper(),
                            "game": row[3].upper(),
                            "avg_points": row[4].upper(),
                            "team_abbr": row[5].upper()})
    return players[1:]


print "Starting optimization..."

print "Reading players..."
players = parse_players("data/nfl/salaries.csv")

print "Starting Engine..."
season = 2015
week = 13
nfl.engine.start(season, week, players)

print "FINISHED!"
