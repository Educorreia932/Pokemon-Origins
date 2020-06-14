import csv

origin = {}

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    for row in reader:
        if row[1] != "":
            if row[1] not in origin:
                origin[row[1]] = [row[0]]
                
            else:
                origin[row[1]].append(row[0])
                
    print(origin)