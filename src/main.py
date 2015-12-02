import csv
import nfl.engine
from nfl.player import Player


def parse_players(file_name):
    players = []
    with open(file_name, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            player = Player(row[0], row[1], row[2], row[3], row[4], row[5])
            players.append(player)
    return players[1:]


print "Starting optimization..."

print "Reading players..."
players = parse_players("data/nfl/salaries.csv")

print "Starting Engine..."
season = 2015
week = 13
nfl.engine.start(season, week, players)

print "FINISHED!"
