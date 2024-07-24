import csv
import statistics
import math

spring = []
fall = []

csv ="sample_grades_original.csv"

file=open(csv)
for line in file:
    list = line.rstrip().split(",")
    if len(list)>1:
        spring.append(eval(list[2]))
        print(list[0], list[2])
    # print(list[1])
    # print(list[2])






# Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }
#
# print("Dictionary items:")
#
# # Printing all the items of the Dictionary
# print(Dictionary1.items())

##Linda Franklin 07-23-2024
