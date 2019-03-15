
import csv

pypolldict = dict()
with open('02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv',newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        pypolldict[ row['Voter ID'] ] = [row['County'],row['Candidate']]

# Schema: Voter ID , Country , Candidate
pypolldict['12864552'][1]

#The total number of votes cast
len(pypolldict)

# A complete list of candidates who received votes
s = set()
for i in pypolldict.values():
    s.add(i[1])

s

# The percentage of votes each candidate won
dd = {}

for i in s:
    sum = 0
    for j in pypolldict.values():
        if i == j[1]:
            sum = sum + 1
    dd[i] = sum

dd

# The percentage of votes each candidate won
dd = {}
# sum = 0 , the incorrect way
for i in s:
    sum = 0 # the correct way
    for j in pypolldict.values():
        if i == j[1]:
            sum = sum + 1
    dd[i] = (sum/len(pypolldict)) * 100

dd