from data import ATTACK_DATA, CREATURE_DATA
import random

class Creature:
    def __init__(self, name, level):
        # here we save variables as basic attributes
        self.name = name
        self.level = level
        self.paused = False
        # we set up the stats using the data file
        self.type = CREATURE_DATA[name]['stats']['type']
        self.base_stats = CREATURE_DATA[name]['stats']
        self.health = self.base_stats['max_health'] * self.level
        self.moves = CREATURE_DATA[name]['moves']
        # here we configure exp, levelups and evolutions
        self.exp = 0
        self.levelup = self.level * 150
        self.evolution = CREATURE_DATA[self.name]['evolve']
    def __repr__(self):
        return f'creature: {self.name}, lvl: {self.level}'
    
    def get_stat(self, stat):
        return self.base_stats[stat] * self.level
    def get_stats(self):
        return {
            'health': self.get_stat('max_health'),
            'attack': self.get_stat('attack'),
            'defence': self.get_stat('defence'),
            'regeneration': self.get_stat('regeneration'),
            'speed': self.get_stat('speed')
        }
    