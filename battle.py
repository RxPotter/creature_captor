from data import ATTACK_DATA

class Battle:
    def __init__(self, player_creature, enemy_creature, end_battle):
        # define general variables for battle
        self.creature_data = {'player': player_creature, 'enemy': enemy_creature}
        self.end_battle = end_battle
        self.battle_over = False

        # define variables for battle control
        self.active_creature = None
        self.indexes = {
            'fight': 0,
            'check team': 0,
            'catch': 0,
            'run': 0
        }
    def battle_menu(self):   
        self.battle_menu = {
            0: 'Fight',
            1: 'Check Team',
            2: 'Catch',
            3: 'Run'
        }
        return self.battle_menu
  