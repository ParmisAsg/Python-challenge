
import csv

d = dict() # an empty dictionary , d = {}

with open('02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv',newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        d[ row['Date'] ] = row['Profit/Losses']

        d

int(d['Jul-2016']) + int(d['Feb-2017'])

len(d.keys())

# The net total amount of "Profit/Losses" over the entire period
sum = 0
for i in d.values():
    sum = sum + int(i)
print(sum)

# The average of the changes in "Profit/Losses" over the entire period
first = d['Jan-2010']
last = d['Feb-2017']
changes = list() # or you simply could have wrote // changes = [] //

p = 0
for i in d.values():
    changes.append( int(i) - p)
    p = int(i)

p = 0
for i in changes[1:]:
    p = p + i
result = p / len(changes)

round(result,3)

# The greatest increase in profits (date and amount) over the entire period
max(changes)

# The greatest decrease in losses (date and amount) over the entire period
min(changes)

print('Financial Analysis')
print('----------------------------')
print('Total Months: ',str(len(d.keys())))
print('Total: ',str(sum))
print('Average  Change: ',str(round(result,3)))
print('Greatest Increase in Profits: ',str(max(changes)))
print('Greatest Decrease in Profits: ',str(min(changes)))





