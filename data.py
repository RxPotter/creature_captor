CREATURE_DATA = {
    'Blaze Adder': {
        'stats': {'type': 'Heat','max_health': 12, 'attack': 12, 'defence': 8, 'catch_rate': 90, 'speed': 15},
        'moves': {0: 'Scorch',1: 'Tackle',5: 'Glide',7: 'Bite'},
        'evolve': ('Fire Viper', 16)},
    'Fire Viper': {
        'stats': {'type': 'Heat','max_health': 20, 'attack': 25, 'defence': 12, 'catch_rate': 30, 'speed': 25},
        'moves': {0: 'Scorch',1: 'Tackle',5: 'Glide',7: 'Bite'},
        'evolve': None},
    'Frostbite': {
        'stats': {'type': 'Water','max_health': 15, 'attack': 10, 'defence': 15, 'catch_rate': 90, 'speed': 8},
        'moves': {0: 'Spray',1: 'Tackle',5: 'Glide',7: 'Bite'},
        'evolve': ('Ice Hound', 17)},
    'Ice Hound': {
        'stats': {'type': 'Water','max_health': 25, 'attack': 16, 'defence': 25, 'catch_rate': 30, 'speed': 10},
        'moves': {0: 'Spray',1: 'Tackle',5: 'Glide',7: 'Bite'},
        'evolve': None},
    'Thornback': {
        'stats': {'type': 'Plant','max_health': 10, 'attack': 10, 'defence': 10, 'catch_rate': 90, 'speed': 10},
        'moves': {0: 'Thorn',1: 'Tackle',5: 'Glide',7: 'Bite'},
        'evolve': ('Thornspike', 16)},
    'Thornspike': {
        'stats': {'type': 'Plant','max_health': 22, 'attack': 22, 'defence': 20, 'catch_rate': 30, 'speed': 20},
        'moves': {0: 'Thorn',1: 'Tackle',5: 'Glide',7: 'Bite'},
        'evolve': None},
}

ATTACK_DATA = {
    'Scorch': {'type': 'Heat', 'power': 10, 'accuracy': 90, 'max_uses': 20, 'effect': 'burn', 'effect_chance': 10},
    'Spray':  {'type': 'Water', 'power': 5, 'accuracy': 100, 'max_uses': 25, 'effect': 'none', 'effect_chance': 0},
    'Thorn':  {'type': 'Plant', 'power': 8, 'accuracy': 90, 'max_uses': 20, 'effect': 'none', 'effect_chance': 0},
    'Glide':  {'type': 'Air', 'power': 5, 'accuracy': 100, 'max_uses': 25, 'effect': 'none', 'effect_chance': 0},
    'Tackle': {'type': 'Normal', 'power': 8, 'accuracy': 95, 'max_uses': 30, 'effect': 'none', 'effect_chance': 0},
    'Bite':   {'type': 'Normal', 'power': 12, 'accuracy': 85, 'max_uses': 25, 'effect': 'none', 'effect_chance': 0},


}