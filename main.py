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
    global game_end
    while game_end == False:
        checkPaths()
        print("Where would you like to go?")
        user_input = input("")
        movement(int(user_input))
        if input == -1:
            game_end = True
def movement(user_input):
    if user_input == 1:
        try:
            player1.y -= 1
        except:
            print("You cannot move North")
    if user_input == 2:
        try:
            player1.x += 1
        except:
            print("You cannot move East")
    if user_input == 3:
        try:
            player1.y += 1
        except:
            print("You cannot move South")
    if user_input == 4:
        try:
            player1.y -= 1
        except:
            print("You cannot move West")
    
def checkPaths():
    if player1.y !=0:
        if mapData[player1.y - 1][player1.x] != 0:
            print("1: North")
    if player1.y != len(mapData) - 1:
        if mapData[player1.y][player1.x + 1] != 0:
            print("2: East")
    if player1.y != len(mapData) - 1:
        if mapData[player1.y + 1][player1.x] != 0:
            print("3: South")
    if player1.x != 0:
      if mapData[player1.y][player1.x - 1] != 0:
         print("4: West")

def creature_encouter():
    Battle.__init__(Battle, player1.player_creatures[0], Creature(random_creature, 10), 0)
    Battle.battle_start(Battle)
#print(player1)
player1.player_creatures.append(Creature('Blaze Adder', 10))
random_creature = random.choice(list(CREATURE_DATA.keys()))
#print(random_creature)
#print(player1.player_creatures)

explore_loop()

