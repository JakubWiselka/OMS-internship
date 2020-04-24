import random


class Person():
    def __init__(self, name, surname, age, isAlive, coins):
        self.name = name
        self.surname = surname
        self.age = age
        self.isAlive = isAlive
        self.coins = coins
        
    def addAge(self, age):
        self.age += 1
    
    def stats(self):
        return self.name, self.surname, self.age, self.isAlive, self.coins

class Villager(Person):
    def __init__(self, name, surname, age, isAlive, coins, profession):
        super().__init__(name, surname, age, isAlive, coins)
        self.profession = profession
        
    def work(self):
        super().addAge(self.age)
        self.coins += 100
        

class Warrior(Person):
    def __init__(self, name, surname, age, isAlive, coins, weapon, position):
        super().__init__(name, surname, age, isAlive, coins)
        self.weapon = weapon
        self.position = position
        self.strength = random.randint(1, 9)
        
    def stats(self):
        return super().stats(), self.strength, self.position, self.weapon
        
class Commandor(Person):
    def __init__(self, name, surname, age, isAlive, coins, warriors = None):
        super().__init__(name, surname, age, isAlive, coins)
        if warriors == None:
            self.warriors = []
        else:
            self.warriors = warriors
    
    def addWarrior(self, war):
        if war not in self.warriors:
            self.warriors.append(war)
            
    def removeWarrior(self, war1):
        for war in self.warriors:
            if war.isAlive == False:
                # print(war.name)
                self.warriors.remove(war)
            
    def printWarriors(self):
        for w in self.warriors:
            print('-> ' + str(w.stats()))









def fight(com_1 ,com_2, war_obj_1, war_obj_2):
    lenght = len(war_obj_1)
    for x in range(lenght):
        if war_obj_1[x].strength == war_obj_2[x].strength:
            war_obj_1[x].isAlive = False
            war_obj_2[x].isAlive = False
            
        elif war_obj_1[x].strength < war_obj_2[x].strength:
            war_obj_2[x].strength = war_obj_2[x].strength - war_obj_1[x].strength
            war_obj_1[x].isAlive = False
            
        else:
            war_obj_1[x].strength -= war_obj_2[x].strength
            war_obj_2[x].isAlive = False
  
    com_1.removeWarrior(war_obj_1)
    com_2.removeWarrior(war_obj_2)
    
    
    
    com_1.printWarriors()
    print("")
    com_2.printWarriors()
            
    
            
        
        
 
            
        












def villageRun():
    war_1 = []
    war_1.append(["Bob","Briggs", 26, True, 160, "sword", "offensive"])
    war_1.append(["Henry","Schmitt", 31, True, 530, "sword", "offensive"])
    war_1.append(["Dave","Smith", 23, True, 234, "sword", "offensive"])
    war_1.append(["Mark","Weiss", 28, True, 123, "sword", "offensive"])
    war_1.append(["Henry","Schmitt", 31, True, 513, "bow", "defense"])
    war_1.append(["Henry","Schmitt", 31, True, 563, "bow", "defense"])
    war_1.append(["Donnie","Qualls", 19, True, 60, "bow", "defense"])
    
    war_obj_1 = list()
    for w in war_1:
        war_obj_1.append(Warrior(w[0], w[1], w[2], w[3], w[4], w[5], w[6]))
    
    # print(len(war_obj_1))
    
    
    war_2 = []
    war_2.append(["Edwards","Pratt", 26, True, 160, "sword", "offensive"])
    war_2.append(["Goodwin","Mason", 31, True, 530, "sword", "offensive"])
    war_2.append(["Simmons","Higgins", 23, True, 234, "sword", "offensive"])
    war_2.append(["Pacheco","Mendoza", 28, True, 123, "sword", "offensive"])
    war_2.append(["Gardner","Drake", 31, True, 513, "bow", "defense"])
    war_2.append(["Ortiz","Marsh", 31, True, 563, "bow", "defense"])
    war_2.append(["Duran","Bass", 19, True, 60, "bow", "defense"])
    
    war_obj_2 = list()
    for w in war_2:
        war_obj_2.append(Warrior(w[0], w[1], w[2], w[3], w[4], w[5], w[6]))
        
    # print(len(war_obj_2))
    
    com_1 = Commandor("David", "Ironsword", 35, True, 4000, war_obj_1)
    # com_1.printWarriors()
    
    com_2 = Commandor("Gregg", "Knight", 51, True, 4000, war_obj_2)
    # com_2.printWarriors()

    fight(com_1, com_2, war_obj_1, war_obj_2)





villageRun()




    