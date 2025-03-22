import csv
from player import*
from data import*
from creatureFramework import Creature
from battle import*
import random
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
 

def checkPaths():
    for i, x in enumerate(directions):
        if mapData[player1.x + 1][player1.y] != 0:
            print(f"{i+1}.", x)
            #int(input('pick a direction: '))
        else:
            break
def creature_encouter():
    pass
#print(player1)
player1.player_creatures.append(Creature('Blaze Adder', 10))
random_creature = random.choice(list(CREATURE_DATA.keys()))
#print(random_creature)
#print(player1.player_creatures)
Battle.__init__(Battle, player1.player_creatures[0], Creature(random_creature, 10), 0)
Battle.battle_start(Battle)

