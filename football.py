import csv, math, ast, numpy as np

# We have defined the function called poisson. Passing in two variables which we need to provide when we use it.

# Next is a calculation of the probability of 'actual' amounts of goals scored, when the mean is equal to 'mean'.
# This writes out the probability 'p'.

# Next we have defined the data we want to use, the 2020/2021 season in csv format.
# We then create an empty list called team_list. We then open a file called team_list.txt and use the 'w' tag
# after the name to ensure at all the info is deleted.

def poisson(actual, mean):
    return math.pow(mean, actual) * math.exp(-mean) / math.factorial(actual)

csvFile = '20202021.csv'

team_list = []

k = open('team_list.txt', 'w')
k.write("""{
""")
