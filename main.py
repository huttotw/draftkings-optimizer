# 0/1 knapsack
import csv
import itertools
import math
import sys
import re


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def parse_defenses(file_name):
    defense = []
    with open(file_name, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            defense.append(row[1])
    return defense[1:]


def parse_players(file_name):
    players = []
    with open(file_name, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            players.append((row[0], row[1], row[2], row[3], row[4], row[5]))
    return players[1:]


def pick_teams(sport, players):
    if sport == "NFL":
        numOfPositions = 9
    elif sport == "NBA":
        numOfPositions = 8

    numOfCombinations = nCr(len(players), numOfPositions)

    for i, team in enumerate(itertools.combinations(players, numOfPositions)):
        progress = "\r[{0}/{1}]".format(i, numOfCombinations)
        sys.stdout.write(progress)
        sys.stdout.flush()
        if does_team_have_positions(sport, team) and does_team_fit_cap(team):
            check_current_best(team)


def does_team_have_positions(sport, team):
    positions = []
    for players in team:
        positions.append(players[0])

    if sport == "NFL":
        try:
            positions.remove("QB")
            positions.remove("RB")
            positions.remove("RB")
            positions.remove("WR")
            positions.remove("WR")
            positions.remove("WR")
            positions.remove("RB")
            positions.remove("TE")
            positions.remove("DST")
        except ValueError:
            return False

    elif sport == "NBA":
        try:
            positions.remove("PG")
            positions.remove("SG")
            positions.remove("SF")
            positions.remove("PF")
            positions.remove("C")
            positions.remove("PG")
            positions.remove("SF")
            positions.remove("SG")
        except ValueError:
            return False

    if len(positions) == 0:
        return True
    else:
        return False


def adjust_values(players, defenses):
    adjusted_players = []
    for player in players:
        game = player[3]  # get the game info
        teams = re.search("^(\S+)@(\S+)\s", game)  # separate into 2 teams
        team1 = teams.group(1)  # get the first team
        team2 = teams.group(2)  # get the second team

        # get the opponent
        if team1 == player[5]:
            opponent = team2
        else:
            opponent = team1

        opponent_rank = defenses.index(opponent)
        adjusted_value = float(opponent_rank) / float(len(defenses)) * float(player[4])
        adjusted_players.append((player[0], player[1], player[2], player[3], adjusted_value, player[5]))

    return adjusted_players


def get_team_salary(team):
    salaries = []
    for players in team:
        salaries.append(players[2])

    salaries = map(int, salaries)

    return sum(salaries)


def get_team_value(team):
    values = []
    for players in team:
        values.append(players[4])

    values = map(float, values)

    return sum(values)


def does_team_fit_cap(team):
    salary = get_team_salary(team)

    if salary <= 50000:
        return True
    else:
        return False


def check_current_best(team):
    global max_value
    value = get_team_value(team)
    if value >= max_value:
        display_team(team)
        max_value = value


def display_team(team):
    print "###################### Current Best #######################"
    print "{0:10} {1:20} {2:7} {3:10}".format("Pos", "Name", "Salary",
                                              "TPA")
    for player in team:
        print "{0:10} {1:20} {2:7} {3:10}".format(player[0], player[1],
                                                  player[2], player[4])
    print "Total Salary: " + str(get_team_salary(team))
    print "Expected Team TPA: " + str(get_team_value(team))


max_value = 0
max_salary = 0
print "Starting optimization..."
print "Reading players..."
# NFL
players = parse_players("data/nfl/salaries.csv")
# NBA
# players = parse_players("data/nba/salaries.csv")

print "Reading defenses..."
defenses = parse_defenses("data/nfl/defenses.csv")

print "Adjusting values..."
players = adjust_values(players, defenses)

print "Looking for best teams..."
# NFL
pick_teams("NFL", players)
# NBA
# pick_teams("NBA", players)
print "FINISHED!"
