import time
import numpy as np
import sys

class Creature:
    def __init__(self, name, types, moves, IVs, health='==================='):
        # here we save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = IVs['ATTACK']
        self.defence = IVs['DEFENCE']
        self.health = health
        self.bars = 20 # Set number of health bars

    def fight(self, Creature2):
        #this function allows two creature to fight eachother
        #print fight info
        print("-----CREATURE COMBAT-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENCE/", self.defence)
        print("\nVS")
        print(f"\n{Creature2.name}")
        print("TYPE/", Creature2.types)
        print("ATTACK/", Creature2.attack)
        print("DEFENCE/", Creature2.defence)

        time.sleep(2)

        #Creating type advantage
        version = ['Heat', 'Aqua', 'Arbor']
        for i,k in enumerate(version):
            if self.types == k:
                #When both Creatures are the same type
                if Creature2.types == k:
                    str1_attack = "It's not very effective"
                    str2_attack = "It's not very effective"
                
                # When Creature2 is strong against creature 1
                if Creature2.types == version[(i+1)%3]:
                    Creature2.attack *= 2

                    self.attack /=2

                    str1_attack = "It's not very effective"
                    str2_attack = "It's super effective!"

                # When Creature2 is weak against creature 1
                if Creature2.types == version[(i+2)%3]:
                    self.attack *=2

                    Creature2.attack /= 2

                    str1_attack = "It's super effective!" 
                    str2_attack = "It's not very effective"
        def turnAttack(self, Creature2):
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('pick a move: '))
            print(f"{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            print(str1_attack)

            # here we determine damage
            Creature2.bars -= self.attack
            Creature2.health = ""

            # here we add bars back
            for j in range(int(Creature2.bars)):
                Creature2.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Creature2.name}\t\tHLTH\t{Creature2.health}")
            time.sleep(.5)            
        # 
        while (self.bars > 0) and (Creature2.bars > 0):
            #print health of both creatures
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Creature2.name}\t\tHLTH\t{Creature2.health}")

            print(f"Go {self.name}!")
            turnAttack(self, Creature2)

            # Here we check if creature fainted
            if Creature2.bars <= 0:
                print("\n..." + Creature2.name + 'fainted.')
                break
            turnAttack(Creature2, self)
            if self.bars <= 0:
                print("\n..." + self.name + 'fainted.')
                break

if __name__ == '__main__':
    Blaze_Adder = Creature('Blaze Adder', 'Heat', ['Scorch', 'Glide', 'Tackle', 'Bite'], {'ATTACK':12, 'DEFENCE':8})

    Blaze_Adder.fight(Blaze_Adder)