'''
Inheritance example
We can do better
# Eevee(Normal), Vaporeon(Water), Jolteon(Eletric), Flareon(Fire)
'''

class Eevee:
    def __init__(self, poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp):
        self.__poke_name = poke_name
        self.__poke_type = poke_type
        self.__poke_weight = poke_weight
        self.__poke_height = poke_height
        self.__poke_cp = poke_cp
        self.__poke_hp = poke_hp
    
    @property
    def poke_name(self):
        return self.__poke_name
    
    @poke_name.setter
    def poke_name(self, poke_name):
        self.__poke_name = poke_name

    @property
    def poke_hp(self):
        return self.__poke_hp
    
    @poke_hp.setter
    def poke_hp(self, poke_hp):
        self.__poke_hp = poke_hp

    def first_skill(self):
        print ('Quick Attack')
        return ('Water Gun', 5)

    def second_skill(self):
        print ('Body Slam')
        return ('Body Slam', 100)

class Vaporeon(Eevee):
    def __init__(self, poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp):
        super().__init__(poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp)

    def first_skill(self):
        print ('Water Gun')
        return ('Water Gun', 5)

    def second_skill(self):
        print ('Hydro Pump')
        return ('Hydro Pump', 100)

class Flareon(Eevee):
    def __init__(self, poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp):
        super().__init__(poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp)
    
    def first_skill(self):
        print ('Ember')
        return ('Ember', 5)

    def second_skill(self):
        print ('Fire Blast')
        return ('Fire Blast', 100)

def main():
    eevee = Eevee('eevee', 'Normal', 30, 30, 30, 30)
    vaporeon = Vaporeon('vaporeon', 'Water', 30, 30, 30, 30)
    flareon = Flareon('flareon', 'Fire', 30, 30, 30, 30)
    eevee.first_skill()
    vaporeon.first_skill()
    flareon.first_skill()

    vaporeon.poke_name = ('kobe')
    vaporeon.poke_hp = (90)
    print (vaporeon.poke_name)
    print (vaporeon.poke_hp)
    

if __name__ == '__main__':
    main()