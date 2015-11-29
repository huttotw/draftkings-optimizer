# 0/1 knapsack
import csv
import itertools


def parse_csv(file_name):
    players = []
    with open(file_name, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            players.append((row[0], row[1], row[2], row[4]))
    return players[1:]


def pick_teams(players):
    for team in itertools.combinations(players, 9):
        does_team_fit_cap(team)
        if does_team_have_positions(team) and does_team_fit_cap(team):
            check_current_best(team)
    return teams


def does_team_have_positions(team):
    positions = []
    for players in team:
        positions.append(players[0])

    try:
        positions.remove("QB")
        positions.remove("RB")
        positions.remove("RB")
        positions.remove("WR")
        positions.remove("WR")
        positions.remove("WR")
        positions.remove("WR")
        positions.remove("TE")
        positions.remove("DST")
    except ValueError:
        return False

    if len(positions) == 0:
        return True
    else:
        return False


def get_team_salary(team):
    salaries = []
    for players in team:
        salaries.append(players[2])

    salaries = map(int, salaries)

    return sum(salaries)


def get_team_value(team):
    values = []
    for players in team:
        values.append(players[3])

    values = map(float, values)

    return sum(values)


def does_team_fit_cap(team):
    salary = get_team_salary(team)

    if salary <= 50000 and salary >= 40000:
        return True
    else:
        return False


def check_current_best(team):
    global max_value
    value = get_team_value(team)
    if value > max_value:
        display_team(team)
        max_value = value


def display_team(team):
    print "###################### Current Best #######################"
    print "{0:10} {1:20} {2:7} {3:10}".format("Pos", "Name", "Salary",
                                              "Avg Points")
    for player in team:
        print "{0:10} {1:20} {2:7} {3:10}".format(player[0], player[1],
                                                  player[2], player[3])
    print "Total Salary: " + str(get_team_salary(team))
    print "Expected Value: " + str(get_team_value(team))


max_value = 0
print "Starting optimization..."
players = parse_csv("data/nfl/salaries.csv")
print "Finished reading teams..."
print "Looking for best teams..."
pick_teams(players)
print "FINISHED!"
