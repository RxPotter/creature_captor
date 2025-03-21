from data import ATTACK_DATA

class Battle:
    def __init__(self, player_creature, enemy_creature, end_battle):
        self.creature_data = {'player': player_creature, 'enemy': enemy_creature}
        self.end_battle = end_battle
        self.battle_over = False

    def setup_battle(self):
        self.player = self.creature_data['player']
        self.enemy = self.creature_data['enemy']
        self.player_health = self.player.stats['max_health']
        self.enemy_health = self.enemy.stats['max_health']
        self.player_moves = self.player.moves
        self.enemy_moves = self.enemy.moves
        