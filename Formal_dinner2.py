import csv
import random

students = []
rows, cols = (36, 7)
table = []
filled = [[0]*cols]*rows
tablecount = 0
waiters = []
kitchen = []

with open('Student_List.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = -1
    for row in csv_reader:
        students.append(row[1] + ' ' + row[0])
        line_count += 1
    students[0] = "Daanish Ahmad"
    for i in range(rows):
        rand = random.randint(0,len(students)-1)
        waiters.append(students[rand])
        students.remove(students[rand])
    for i in range(7):
        rand = random.randint(0,len(students)-1)
        kitchen.append(students[rand])
        students.remove(students[rand])
    while len(students) > 0:
        for i in range(7):
            if len(students) != 0:
                x = random.randint(0,len(students)-1)
                table.append(students[x])
                students.remove(students[x])
        filled[tablecount] = table
        table = []
        tablecount += 1
    print("Tables: ")
    print(filled)
    print()
    print("Waiters: ")
    print(waiters)
    print()
    print("Kitchen Crew:")
    print(kitchen)
