import csv
from player import*
from data import*
from creatureFramework import Creature
import battle
directions = ['North', 'East', 'South', 'West']
def convertCSVto2Dlist(csvFile: str):
    tileMap = []
    with open(csvFile, 'r', newline='') as file:
        for mapRow in csv.reader(file):
            tileMap.append(list(map(int, mapRow)))
    return tileMap
mapData = convertCSVto2Dlist(csvFile = "map.csv")     
start_y = len(mapData) - 1 
start_x = 0
player1 = Player("Gaia", start_x, start_y)
 
battle_menu = {
    0: 'Fight',
    1: 'Check Team',
    2: 'Catch',
    3: 'Run'
    }
def checkPaths():
    for i, x in enumerate(directions):
        if mapData[player1.x + 1][player1.y] != 0:
            print(f"{i+1}.", x)
            #int(input('pick a direction: '))
        else:
            break
def creature_encouter():
    pass
print(player1)
print(player1.player_creatures)

for i in battle_menu:
    print(f"{i+1}.", battle_menu[i])
