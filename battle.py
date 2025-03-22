from data import ATTACK_DATA
from player import *
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
        self.active_creature = [self.creature_data['player']]
        self.enemy_creature = self.creature_data['enemy']
        for i in self.battle_menu:
            print(f"{i+1}.", self.battle_menu[i])

    def apply_attack(self, attack, target, damage):
        attack_type = ATTACK_DATA[attack]['type']
        target_type = target.creature.type

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
        
        target.creature.health -= damage- target.creature.base_stats['defence']
        self.check_death()

        def check_death(self):
            for creature in Player.player_creatures:
                if creature.health <= 0:
                    print(f"{creature.name} has fainted!")
                active_creature = self.active_creature
                available_creatures = [(index, creature) for index, creature in self.creature_data['player'].items() if creature.health > 0 and (index, creature) not in active_creature]
                

                if self.enemy_creature.health <= 0:
                    print(f"{self.enemy_creature.name} has fainted! \n You win!")
                    self.battle_over = True
                
