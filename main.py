import csv
from player import*
from data import*
from creatureFramework import Creature
from battle import*
import random
directions = ['North', 'East', 'South', 'West']
game_end = False
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
 
def explore_loop():
        while game_end == False:

def checkPaths():
    if mapData[player1.y - 1][player1.x] == 1:
        print("1: North")
    if mapData[player1.y][player1.x + 1] == 1:
        print("2: East")
    if mapData[player1.y + 1][player1.x] == 1:
        print("3: South")
    if mapData[player1.y][player1.x - 1] == 1:
        print("4: West")

def creature_encouter():
    pass
#print(player1)
player1.player_creatures.append(Creature('Blaze Adder', 10))
random_creature = random.choice(list(CREATURE_DATA.keys()))
#print(random_creature)
#print(player1.player_creatures)
#Battle.__init__(Battle, player1.player_creatures[0], Creature(random_creature, 10), 0)
#Battle.battle_start(Battle)

