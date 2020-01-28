import csv
import random

def write(filled, waiters, kitchen, file):
    with open(file, 'w') as csvfile:
        fw = csv.writer(csvfile, delimiter=' ')
        for i in range(len(filled)-1):
            fw.writerow(' ')
            fw.writerow('Table ' + str(i + 1) + ':')
            fw.writerow(' ')
            for j in range(7):
                fw.writerow(filled[i][j])
            fw.writerow(waiters[i] + '(W)')
        fw.writerow(' ')
        fw.writerow("Kitchen Crew:")
        for i in kitchen:
            fw.writerow(i)
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
        line_count = -1
        for row in csv_reader:
            students.append(row[1] + ' ' + row[0])
            line_count += 1
        students[0] = "Daanish Ahmad"

    return students
def fill(students):
    rows, cols = (36, 7)
    table = []
    filled = [[0]*cols]*rows
    tablecount = 0
    waiters = []
    kitchen = []

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
    return filled,waiters,kitchen
def out(filled, kitchen, waiters):
    print("Tables: ")
    print(filled)
    print()
    print("Waiters: ")
    print(waiters)
    print()
    print("Kitchen Crew:")
    print(kitchen)

file = 'student_list.csv'
students = read(file)
filled,waiters,kitchen = fill(students)
write(filled,waiters,kitchen, 'FDTables.csv')
out(filled, kitchen, waiters)
