import csv
from player import*

directions = ['North', 'East', 'South', 'West']
def convertCSVto2Dlist(csvFile: str):
    tileMap = []
    with open(csvFile, 'r', newline='') as file:
        for mapRow in csv.reader(file):
            tileMap.append(list(map(int, mapRow)))
    return tileMap
mapData = convertCSVto2Dlist(csvFile = "map.csv")     

player1 = Player("Gaia", mapData[14][0], mapData[14][0])
def checkPaths():
    for i, x in enumerate(directions):
        if mapData[player1.x + 1][player1.y] != 0:
            print(f"{i+1}.", x)
            #int(input('pick a direction: '))
        else:
            break
print(player1)
checkPaths()
