import csv
import matplotlib.pyplot as plt

origins = {}

# Read data file

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    for row in reader:
        if row[1] != "" and row[1] != "Origin":
            if row[1] not in origins:
                origins[row[1]] = [row[0]]
                
            else:
                origins[row[1]].append(row[0])
                
# Graph plotting

origin_name = list(origins)
number_of_pokemon = list(len(origin) for origin in origins)

plt.bar(origin_name, number_of_pokemon)
plt.xticks(rotation = "vertical")
plt.ylabel("Number of pokémon")
plt.title("Pokémon Origins")

plt.show()