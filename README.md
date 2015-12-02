# draftkings-optimizer

## To run this project locally:
* Setup a virtual environment by running `virtualenv venv`, then `source venv/bin/activate`, for more information [virtualenv](https://virtualenv.readthedocs.org/en/latest/)
* Install the dependencies with `pip install -r requirements.txt`
* Download the latest CSV of Draft King player data from contest you want to compete in.
* Place the CSV file at `data/nfl/salaries.csv`
* Run `python src/main.py`

_The program will take several minutes to complete even with a relatively small roster size._
For more information on this type of problem, see [Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem)

## Ways to improve
The program consists of three main components:
* Trimmers
* Adjusters
* Algorithms

### Trimmers
Trimmers are used to shorten the input CSV file. A trimmer can be used to eliminate players that score 0 points on average, or eliminate players from a team you hate. This is an extremely important step, I have found that getting the roster to 36 players yields an acceptable run time, ~15 minutes. With even 40 players, we are looking at 273,438,880 possible teams to sort through.
* Trimmers take in a list of `players`, and return a list of `players`.

### Adjusters
Adjusters are used to make changes to a players estimated value. For instance, you may see that the player is playing against the best defense in the league. You may want to decrease his estimated value. These type of stats can be retrieved from the `nfl.stats` module, also included in the project.
* If you want to add an external data source, do it here after adding it to `nfl.stats`
* Adjusters take in a list of `players`, and return a list of `players`.

### Algorithms
Algorithms are used to compare one team to another. For the sake of space, we have to compare on the fly. This means, we can only compare to the last team generated to see if it was better. The default algorithm is to maximize team value based on the player values. I have had mediocre success by maximizing the salary instead.
* **No stat retrieval should be done here. New data is only added in the adjusters.** This is strictly a function for comparisons.
* Algorithms take in a list of `players` and outputs the best team each time it finds one better than the last.

## Contributing
Contributions are more than welcome, please submit a pull request with any new ways of finding teams, new trimmers, adjusters or algorithms.
