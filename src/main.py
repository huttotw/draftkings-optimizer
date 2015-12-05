import csv
import getopt
import nfl.engine
from nfl.player import Player
import sys


def parse_players(file_name):
    players = []
    with open(file_name, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        headers = next(reader)
        for row in reader:
            player = Player(row[0], row[1], row[2], row[3], row[4], row[5])
            players.append(player)
    return players


def main(argv):
    season = ""
    week = ""
    try:
        opts, args = getopt.getopt(argv, "helps:w:", ["season=", "week="])
    except getopt.GetoptError:
        print "main.py -season <season> -week <week>"
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print "main.py -season <season> -week <week>"
            sys.exit()
        elif opt in ("-s", "--season"):
            season = arg
        elif opt in ("-w", "--week"):
            week = arg

    print "Starting optimization..."

    print "Reading players..."
    players = parse_players("data/nfl/salaries.csv")

    print "Starting Engine..."
    season = 2015
    week = 13
    nfl.engine.start(season, week, players)

    print "FINISHED!"

main(sys.argv[1:])
