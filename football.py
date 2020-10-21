import csv, math, ast, numpy as np

# We have defined the function called poisson. Passing in two variables which we need to provide when we use it.

# Next is a calculation of the probability of 'actual' amounts of goals scored, when the mean is equal to 'mean'.
# This writes out the probability 'p'.

# Next we have defined the data we want to use, the 2020/2021 season in csv format.
# We then create an empty list called team_list. We then open a file called team_list.txt and use the 'w' tag
# after the name to ensure at all the info is deleted.
# Next we write the first line in the file, which is the start of a dictionary. This is to hold and update our data for each team.

def poisson(actual, mean):
    return math.pow(mean, actual) * math.exp(-mean) / math.factorial(actual)

csvFile = '20202021.csv'

team_list = []

k = open('team_list.txt', 'w')
k.write("""{
""")

# Next we want to iterate over our data file and find all the team names that are going to be used.
# This is done like above where we open the csv file, skip the first line and then create a for loop.
# The for loop reads both team names and then checks if the names are in our newly created team_list. If they are not, they get added to the list.
# After it has checked all the team names, it sorts the new list alphabetically.

# The next for loop iterates over over all the teams we find.
# we will record all the home goals and away goals they score, as well as how many goals they concede both at home and away.
# We also track the amount of home and away games.

csvRead = csv.reader(open(csvFile))
next(csvRead)

for row in csvRead:
    if row[2] not in team_list:
        team_list.append(row[2])
    if row[3] not in team_list:
        team_list.append(row[3])

team_list.sort()

for team in team_list:
    k.write("""	'%s': {'home_goals': 0, 'away_goals': 0, 'home_conceded': 0, 'away_conceded': 0, 'home_games': 0, 'away_games': 0, 'alpha_h': 0, 'beta_h': 0, 'alpha_a': 0, 'beta_a': 0},
""" % (team))

# We then write the end of the file and close it. This is so as to save what we have written if we want to open it again.

k.write("}")
k.close()

# The next two lines creates our dictionary where we will hold and update our data we read.
# This is done by using the ast module which will read the team_list.txt file and then create a dictionary called ‘dict’.

s = open('team_list.txt', 'r').read()
dict = ast.literal_eval(s)

GAMES_PLAYED = 0 # This variable is the total tally of games played.
WEEKS_WAIT = 4 # This could be changeable. This is refering to how many weeks we want to wait before placing a bet.
TOTAL_VALUE = 0 # This will be sued to update how our betting is doing.

csvRead = csv.reader(open(csvFile))
next(csvRead)

for
