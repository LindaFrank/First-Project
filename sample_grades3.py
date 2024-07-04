import csv
with open('sample_grades.csv', mode = 'r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)
   



import pandas
csvFile = pandas.read_csv('sample_grades.csv')
print(csvFile)


##import pandas
##csvFile = pandas.read_csv('sample_grades.csv')
####print(csvFile)
##i = 0
##
##while i < len(csvFile):
##    for line in csvFile:
##        print (line, " ",  end="")
##        
##        i += 1
##    print (i)

import pandas
csvFile = pandas.read_csv('sample_grades.csv')

i = 0

while i < len(csvFile):
    for line in csvFile:
        print (line, " ",  end="")
        
        i += 1
    print (i)
