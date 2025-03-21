from creatureFramework import *
class Player:
    player_creatures = []
    def __init__(self, name, x ,y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def __str__(self):
      return f"Name: {self.name}, X: {self.x}, Y: {self.y}"
    
    def add_creature(self, creature):
        self.player_creatures.append(creature)
    