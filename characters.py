import random

# =====================
# Base Character Class
# =====================
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

        self.block_attack = False
        self.special_attack_cooldown = 0
        self.defensive_cooldown = 0

    # -----------------
    # Basic Attack
    # -----------------
    def attack(self, opponent):
        ability_name = "Attack"

        if opponent.block_attack:
            print(f"{opponent.name} blocks the attack!")
            opponent.block_attack = False
            return

        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} uses {ability_name} on {opponent.name} for {damage} damage!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    # -----------------
    # Defensive Ability (Base)
    # -----------------
    def defensive_special_ability(self):
        ability_name = "Block"

        if self.defensive_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.defensive_cooldown} more turn(s)!")
            return False

        print(f"{self.name} uses {ability_name}!")
        self.block_attack = True
        self.defensive_cooldown = 2

        if self.special_attack_cooldown > 0:
            self.special_attack_cooldown -= 1
            print("Special attack cooldown reduced by 1!")

        return True

    # -----------------
    # Special Attack (Base)
    # -----------------
    def special_attack(self, opponent):
        ability_name = "Special Attack"

        if self.special_attack_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.special_attack_cooldown} more turn(s)!")
            return False

        print(f"{self.name} uses {ability_name}!")
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{ability_name} deals {damage} damage!")

        self.special_attack_cooldown = 3
        return True

    # -----------------
    # Heal
    # -----------------
    def heal(self):
        ability_name = "Heal"
        heal_amount = random.randint(15, 25)
        old_hp = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} uses {ability_name} and restores {self.health - old_hp} HP!")

    # -----------------
    # Display
    # -----------------
    def display_stats(self):
        print(
            f"{self.name} | "
            f"HP: {self.health}/{self.max_health} | "
            f"ATK: {self.attack_power} | "
            f"Special CD: {self.special_attack_cooldown} | "
            f"Defense CD: {self.defensive_cooldown}"
        )

    def display_health(self):
        print(f"{self.name} HP: {self.health}/{self.max_health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 140, 25)

    def defensive_special_ability(self):
        ability_name = "Guardian's Shield"

        if self.defensive_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.defensive_cooldown} turn(s)!")
            return False

        print(f"{self.name} raises {ability_name}!")
        if random.randint(1, 100) > 15:
            self.block_attack = True
            self.defensive_cooldown = 2
            print("Attack will be blocked!")

            if self.special_attack_cooldown > 0:
                self.special_attack_cooldown -= 1
                print("Special cooldown reduced by 1!")
        else:
            print("The shield fails!")

        return True

    def special_attack(self, opponent):
        ability_name = "Sword Strike Storm"

        if self.special_attack_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.special_attack_cooldown} turn(s)!")
            return False

        print(f"{self.name} unleashes {ability_name}!")
        damage = self.attack_power + random.choice([10, 20, 30])
        opponent.health -= damage
        print(f"{ability_name} deals {damage} damage!")

        self.special_attack_cooldown = 4
        return True
    

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100, 35)

    def defensive_special_ability(self):
        ability_name = "Forcefield"

        if self.defensive_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.defensive_cooldown} turn(s)!")
            return False

        print(f"{self.name} conjures a {ability_name}!")
        if random.randint(1, 100) > 35:
            self.block_attack = True
            self.defensive_cooldown = 3
            print("The barrier absorbs the next attack!")

            if self.special_attack_cooldown > 0:
                self.special_attack_cooldown -= 1
                print("Special cooldown reduced by 1!")
        else:
            print("The spell fizzles out leaving the mage vunerable!")

        return True

    def special_attack(self, opponent):
        ability_name = "Fireball"

        if self.special_attack_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.special_attack_cooldown} turn(s)!")
            return False

        print(f"{self.name} casts {ability_name}!")
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{ability_name} scorches {opponent.name} for {damage} damage!")

        self.special_attack_cooldown = 2
        return True




# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 120, 25)

    def defensive_special_ability(self):
        ability_name = "Evade"

        if self.defensive_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.defensive_cooldown} turn(s)!")
            return False

        print(f"{self.name} attempts to {ability_name}!")
        if random.randint(1, 100) > 20:
            self.block_attack = True
            self.defensive_cooldown = 1
            print("The attack was evaded!")

            if self.special_attack_cooldown > 0:
                self.special_attack_cooldown -= 1
                print("Special cooldown reduced by 1!")
        else:
            print("Evade failed!")

        return True

    def special_attack(self, opponent):
        ability_name = "Quick Shot"

        if self.special_attack_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.special_attack_cooldown} turn(s)!")
            return False

        print(f"{self.name} fires {ability_name}!")
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{ability_name} hits for {damage} damage!")

        self.special_attack_cooldown = 3
        return True


# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 150, 15)

    def defensive_special_ability(self):
        ability_name = "Divine Shield"

        if self.defensive_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.defensive_cooldown} turn(s)!")
            return False

        print(f"{self.name} invokes {ability_name}!")
        if random.randint(1, 100) > 5:
            self.block_attack = True
            self.defensive_cooldown = 2
            print("Holy light blocks the attack!")

            if self.special_attack_cooldown > 0:
                self.special_attack_cooldown -= 1
                print("Special cooldown reduced by 1!")
        else:
            print("The gods remain silent!")

        return True

    def special_attack(self, opponent):
        ability_name = "Divine Strike"

        if self.special_attack_cooldown > 0:
            print(f"{ability_name} is on cooldown for {self.special_attack_cooldown} turn(s)!")
            return False

        print(f"{self.name} smites the enemy with {ability_name}!")
        damage = self.attack_power + 5
        opponent.health -= damage
        print(f"{ability_name} deals {damage} damage!")
        self.heal()

        self.special_attack_cooldown = 3
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
            print("The wizard regenerates!")
            if self.health == self.max_health:

                
                print(f"The wizard's health is full!")
            elif self.health+5 > self.max_health:
                regeneration_amount = self.max_health - self.health
                self.health = self.max_health
                print(f"The wizard regenerates {regeneration_amount} health!")
            else:
                self.health += 5
                print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        else:
            print("The wizard's regeneration spell failed!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")