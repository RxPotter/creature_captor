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
player1 = Player("", start_x, start_y)
 
def explore_loop():
    global game_end
    while game_end == False:
        checkPaths()
        print("Where would you like to go?")
        user_input = input("")
        movement(int(user_input))
        if input == -1:
            game_end = True
            break
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
    encounter_chance = random.randint(0, mapData[player1.y][player1.x])
    if encounter_chance == 0:
        creature_encouter() 
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
    random_creature = random.choice(list(CREATURE_DATA.keys()))
    player_average_level = sum([creature.level for creature in player1.player_creatures]) / len(player1.player_creatures)
    Battle.__init__(Battle, player1.player_creatures[0], Creature(random_creature, 10), player_average_level + 2)
    Battle.battle_start(Battle)
starter_creature = [Creature('Blaze Adder', 5), Creature('Frostbite', 5), Creature('Thornback', 5)]
print("Hello there! What was your name again?")
player1.name = input("")
print(f"Ah yes! {player1.name}!")
print("Welcome to your new adventure!")
print("The Creatures out there can be dangerous, but with the right partner, you can overcome any challenge!")
print("Who will be the first to accompany you on your journey?")
for i in range(len(starter_creature)):
    print(f"{i+1}. {starter_creature[i].name} lvl {starter_creature[i].level}")
user_input = int(input(""))
player1.player_creatures.append(starter_creature[user_input - 1])
print(f"Wonderful choice, {player1.name}! Now, get out there and explore to your hearts content!")
explore_loop()

