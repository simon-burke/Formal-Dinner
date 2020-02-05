import csv
import random

##writes tables and kitchen crew in csv file
def write(filled, waiters, kitchen, file):
    with open(file, 'w') as csvfile:
        fw = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

##iterate through filled array and copy table and waiter to csv file
        for i in range(len(filled)-1):
            for j in range(7):
                fw.writerow([str(filled[i][j]) + ',' + str(i+1)])
            fw.writerow([str(waiters[i]) + ',W' + str(i+1)])
##iterate through kitchen array and copy to csv
        for i in kitchen:
            fw.writerow([str(i) + ',' + 'kitchen'])

##reads csv file and copy information to arrays
def read(file):
    students = []
    rows, cols = (36, 7)
    table = []
    filled = [[0]*cols]*rows
    tablecount = 0
    waiters = []
    kitchen = []

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            students.append(row[1] + ' ' + row[0])
##removes jibberish around first name read
        students[0] = "Daanish Ahmad"

    return students

##creates first set of tables
def fill(students):
    rows, cols = (36, 7)
    table = []
    filled = [[0]*cols]*rows
    tablecount = 0
    waiters = []
    kitchen = []

##iterate through students and randomly assigns one waiter per table
    for i in range(rows):
        rand = random.randint(0,len(students)-1)
        waiters.append(students[rand])
        students.remove(students[rand])
##iterate through and randomly assign 7 students to kitchen crew
    for i in range(7):
        rand = random.randint(0,len(students)-1)
        kitchen.append(students[rand])
        students.remove(students[rand])
        ##while there are unassigned students, randomly assign 7 students to each table
    while len(students) > 0:
        for i in range(7):
            if len(students) != 0:
                x = random.randint(0,len(students)-1)
                table.append(students[x])
                students.remove(students[x])
        filled[tablecount] = table
        table = []
        tablecount += 1
    return filled,waiters,kitchen

##print output to console
def out(filled, kitchen, waiters):
    print("Tables: ")
    print(filled)
    print()
    print("Waiters: ")
    print(waiters)
    print()
    print("Kitchen Crew:")
    print(kitchen)

##shuffle tables to create second and third seatings
def shuffle(number ,filled, waiters, kitchen):
    ##swap kitchen crew with table members depending on the seating number
    for i in range(7):
        filled[i][number], kitchen[i] = kitchen[i], filled[i][number]
        ##swap waiters with table members
    for i in range(len(filled)):
        filled[i][0], waiters[i] = waiters[i], filled[i][0]
##shuffle table members so that first table member moves up one table, second moves up two tables, etc.
        for j in range(6,0,-1):
            nextTable = i + j + 1
            if nextTable > 35:
                nextTable -= 36
            filled[nextTable].append(filled[i].pop(j))


file = 'student_list.csv'
students = read(file)
filled,waiters,kitchen = fill(students)
write(filled,waiters,kitchen, 'FDTables.csv')
out(filled, kitchen, waiters)
shuffle(1, filled, kitchen, waiters)
write(filled, waiters, kitchen, 'FDTables2.csv')
out(filled, kitchen, waiters)
shuffle(2, filled, kitchen, waiters)
write(filled, waiters, kitchen, 'FDTables3.csv')
out(filled, kitchen, waiters)
