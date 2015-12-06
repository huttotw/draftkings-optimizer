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
    input_file = ""
    try:
        opts, args = getopt.getopt(argv, "helps:w:i:", ["season=", "week=", "input="])
    except getopt.GetoptError:
        print "main.py --season <season> --week <week> --input <input_file>"
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print "main.py --season <season> --week <week> --input <input_file>"
            sys.exit()
        elif opt in ("-s", "--season"):
            season = arg
        elif opt in ("-w", "--week"):
            week = arg
        elif opt in ("-i", "--input"):
            input_file = arg

    print "Starting optimization..."

    print "Reading players..."
    players = parse_players(input_file)

    print "Starting Engine..."
    nfl.engine.start(season, week, players)

    print "FINISHED!"

main(sys.argv[1:])
