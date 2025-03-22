from data import ATTACK_DATA
from player import *
from random import *
class Battle:
    def __init__(self, player_creature, enemy_creature, end_battle):
        # define general variables for battle
        self.creature_data = {'player': player_creature, 'enemy': enemy_creature}
        self.end_battle = end_battle
        self.battle_over = False

        # define variables for battle control
        self.active_creature = None
        self.enemy_creature = None
        self.battle_menu = {
        0: 'Fight',
        1: 'Check Team',
        2: 'Catch',
        3: 'Run'
        }
    def battle_start(self):
        print(f"A wild {self.creature_data['enemy'].name} appeared!")
        print(f"Go {self.creature_data['player'].name}!")
        self.active_creature = [self.creature_data['player']]
        self.enemy_creature = self.creature_data['enemy']
        self.battle_loop(Battle)
    
    def battle_loop(self):
        while self.battle_over == False:
            print(f"{self.active_creature[0].name}\t\tHP:\t{self.active_creature[0].health}")
            print(f"{self.enemy_creature.name}\t\tHP:\t{self.enemy_creature.health}")
            if self.active_creature[0].get_stats()['speed'] > self.enemy_creature.get_stats()['speed']:
                self.player_turn(Battle)
                self.enemy_turn(Battle)
            else:
                self.enemy_turn(Battle)
                self.player_turn(Battle)
    def player_turn(self):
            print("What will you choose to do?")
            for i in self.battle_menu:
                print(f"{i+1}.", self.battle_menu[i])
            choice = int(input(""))
            match choice:
                case 1:
                    self. fight_menu(Battle)
                case 2:
                    print(Player.player_creatures)
                case 3:
                    pass
                case 4:
                    self.battle_over = True
                case _:
                    print("Invalid choice")
    
    def enemy_turn(self):
        move = choice(self.enemy_creature.get_moves())
        print(f"{self.enemy_creature.name} used {move}!")
        self.apply_attack(self, move, self.active_creature[0], ATTACK_DATA[move]['power'])
    
    def fight_menu(self):
        print("Choose a move:")
        for i, move in enumerate(self.active_creature[0].get_moves()):
            print(f"{i+1}.", move)
        choice = int(input(""))
        move = self.active_creature[0].get_moves()[choice-1]
        print(f"{self.active_creature[0].name} used {move}!")
        self.apply_attack(self, move, self.enemy_creature, ATTACK_DATA[move]['power'])

    def apply_attack(self, attack, target, damage):
        attack_type = ATTACK_DATA[attack]['type']
        target_type = target.type

        # attack doubled
        if attack_type == 'Heat' and target_type == 'Plant' or \
        attack_type == 'Water' and target_type == 'Heat' or \
        attack_type == 'Air' and target_type == 'Plant' or \
        attack_type == 'Plant' and target_type == 'Water':
            damage *= 2

        # attack halved
        if attack_type == 'Heat' and target_type == 'Water' or \
        attack_type == 'Water' and target_type == 'Plant' or \
        attack_type == 'Air' and target_type == 'Normal' or \
        attack_type == 'Plant' and target_type == 'Heat':
            damage /= 2
        target_defence = 1 - target.get_stat('defence') / 2000
        target.health -= damage * target_defence
        print(f"{target.name} took {damage} damage!")
        self.check_death(Battle)

    def check_death(self):
                if self.active_creature[0].health <= 0:
                    print(f"{creature.name} has fainted!")
                    active_creature = self.active_creature
                    available_creatures = [(index, creature) for index, creature in enumerate(Player.player_creatures) if creature.health > 0 and (index, creature) not in active_creature]
                    if available_creatures:
                        print("1: Choose a new creature?")
                        print("2: Run")
                        choice = int(input(""))
                        if choice == 2:
                            print("You have no more creatures left!")
                            self.battle_over = True
                    else:
                        print("Who will you send out next?")
                        for i, creature in available_creatures:
                            print(f"{i+1}.", creature)
                        choice = int(input(""))
                        self.active_creature = [available_creatures[choice-1][1]]

                if self.enemy_creature.health <= 0:
                    print(f"{self.enemy_creature.name} has fainted! \n You win!")
                    self.battle_over = True
                
