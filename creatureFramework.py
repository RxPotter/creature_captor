
class Creature:
    def __init__(self, name, types, moves, IVs, health='==================='):
        # here we save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = IVs['ATTACK']
        self.defence = IVs['DEFENCE']
        self.bars = 20 # Set number of health bars


    def fight(self, Creature2):
        #this function allows two creature to fight eachother
        #print fight info
        print("-----CREATURE COMBAT-----")
        print(f"\n{self.name}")
        