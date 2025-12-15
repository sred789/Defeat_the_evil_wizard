import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.block_attack = False
        self.special_attack_cooldown = 0

    def attack(self, opponent):
        if opponent.block_attack:
            print(f"{opponent.name} has blocked the attack!")
            opponent.block_attack = False
            return

        attack_roll = random.randint(self.attack_power-5, self.attack_power+5)
        opponent.health -= attack_roll
        print(f"{self.name} attacks {opponent.name} for {attack_roll} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def defensive_special_ability(self):
        ability_name = "Block"
        print(f"{self.name} uses {ability_name}!")
        self.block_attack = True

    def special_attack(self, opponent):
        ability_name = "Special Attack"
        if self.special_attack_cooldown > 0:
            print(f"{self.name}'s special attack is on cooldown for {self.special_attack_cooldown} more turn(s)!")
            return
        print(f"{self.name} uses {ability_name}!")
        opponent.health -= (self.attack_power+10)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        self.special_attack_cooldown+=3
        print(f"{ability_name} cooldown is {self.special_attack_cooldown}")
        

    def heal(self):
        previous_health = self.health
        self.health += random.randint(15, 25)
        if self.health > self.max_health:
            self.health = self.max_health
        amount_healed = self.health - previous_health
        print(f"{self.name} healed {amount_healed} health!")
        print(f"Current health is {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Special Attack Cooldown: {self.special_attack_cooldown} turns")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def defensive_special_ability(self):
        ability_name = "Guardian's Shield"
        print(f"{self.name} uses {ability_name}!")
        dice_roll = random.randint(0, 100)
        if dice_roll>15:
            self.block_attack = True
            
        else:
            print(f"{self.name} failed to use {ability_name}!")

    def special_attack(self, opponent):
        ability_name = "Sword Strike Storm"
        if self.special_attack_cooldown > 0:
            print(f"{self.name}'s special attack is on cooldown for {self.special_attack_cooldown} more turn(s)!")
            return False
        print(f"{self.name} uses {ability_name}!")
        dice_roll = random.randint(0,100)
        
        if dice_roll <25:
            special_attack_power = (self.attack_power + 10)
        elif dice_roll < 50:
            special_attack_power = (self.attack_power + 20)
        elif dice_roll < 90:
            special_attack_power = (self.attack_power + 30)
        else:
            special_attack_power = (self.attack_power + 35)
        opponent.health -= special_attack_power
        print(f"{self.name} attacks {opponent.name} for {special_attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            return
        self.special_attack_cooldown+=4
        return True
    

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def defensive_special_ability(self):
        ability_name = "Forcefield"
        print(f"{self.name} uses {ability_name}!")
        dice_roll = random.randint(0, 100)
        if dice_roll>35:
            self.block_attack = True
        else:
            print(f"{self.name} failed to use {ability_name}!")

    def special_attack(self, opponent):
        ability_name = "Fire Ball"
        if self.special_attack_cooldown > 0:
            print(f"{self.name}'s special attack is on cooldown for {self.special_attack_cooldown} more turn(s)!")
            return False
        
        print(f"{self.name} uses {ability_name}!")
        opponent.health -= (self.attack_power+15)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

        self.special_attack_cooldown+=2
        return True


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def attack(self, opponent):
        if opponent.block_attack:
            print(f"{opponent.name} has avoided the attack!")
            opponent.block_attack = False
            return
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            return

    def regenerate(self):
        dice_roll = random.randint(1, 100)
        if dice_roll > 5:
            self.health += 5
            print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power= 25)

    def special_attack(self, opponent):
        ability_name = "Quick Shot"
        if self.special_attack_cooldown > 0:
            print(f"{self.name}'s special attack is on cooldown for {self.special_attack_cooldown} more turn(s)!")
            return False
        
        print(f"{self.name} uses {ability_name}!")
        opponent.health -= (self.attack_power*2)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            return
        self.special_attack_cooldown+=3
        return True

    def defensive_special_ability(self):
        ability_name = "Evade"
        print(f"{self.name} uses {ability_name}!")
        dice_roll = random.randint(0, 100)
        if dice_roll>20:
            self.block_attack = True
        else:
            print(f"{self.name} failed to use {ability_name}!")


# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def special_attack(self, opponent):
        ability_name = "Divine Strike"
        if self.special_attack_cooldown > 0:
            print(f"{self.name}'s special attack is on cooldown for {self.special_attack_cooldown} more turn(s)!")
            return False
        
        print(f"{self.name} uses {ability_name}!")
        opponent.health -= (self.attack_power+5)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        self.heal()
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            return
        self.special_attack_cooldown+=3
        return True

    def defensive_special_ability(self):
        ability_name = "Divine Shield"
        print(f"{self.name} uses {ability_name}!")
        dice_roll = random.randint(0, 100)
        if dice_roll>5:
            self.block_attack = True
        else:
            print(f"{self.name} failed to use {ability_name}!")