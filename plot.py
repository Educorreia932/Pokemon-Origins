import csv
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg
import numpy as np

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
number_of_pokemon = list(len(origin) for origin in origins.values())

df = pd.DataFrame({"x": origin_name, "y": number_of_pokemon})
df = df.sort_values("y")

plt.xlim(-0.5, len(df.x))
plt.ylim(0, max(df.y))

plt.xticks(np.arange(len(df.x)), df.x, rotation = "vertical")
plt.ylabel("Number of Pokémon")

# Plotting pokémon sprites
for i, origin_name in enumerate(df.x):
    for j, pokemon_name in enumerate(origins[origin_name]):
        image = mpimg.imread("icons/" + pokemon_name + ".png")
        plt.imshow(image, extent=[i - 0.5, i + 0.5, j, j + 1])

plt.show()