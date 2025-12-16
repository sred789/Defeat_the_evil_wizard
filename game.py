from characters import Warrior, Mage, Archer, Paladin, EvilWizard

def create_character():
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while player.health > 0 and wizard.health > 0:
        turn_end = False

        while not turn_end:
            print("\n--- Your Turn ---")
            print("1. Attack")
            print("2. Special Attack")
            print("3. Defensive Ability")
            print("4. Heal")
            print("5. View Stats")

            choice = input("> ")

            if choice == "1":
                player.attack(wizard)
                wizard.display_health()
                turn_end = True

            elif choice == "2":
                turn_end = player.special_attack(wizard)
                wizard.display_health()

            elif choice == "3":
                turn_end = player.defensive_special_ability()

            elif choice == "4":
                player.heal()
                turn_end = True

            elif choice == "5":
                player.display_stats()
                wizard.display_stats()

        # -------- Enemy Turn --------
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        # -------- Cooldown Tick --------
        if player.special_attack_cooldown > 0:
            player.special_attack_cooldown -= 1
        if player.defensive_cooldown > 0:
            player.defensive_cooldown -= 1

    print("\n--- GAME OVER ---")
    if player.health > 0:
        print("VICTORY!")
    else:
        print("DEFEAT...")

def main():
    player = create_character()
    wizard = EvilWizard("Gorlock")
    battle(player, wizard)

if __name__ == "__main__":
    main()