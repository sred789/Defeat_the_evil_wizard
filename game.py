from characters import Warrior, Mage, Paladin, Archer, EvilWizard

def create_character():
    print("Choose your character class:")
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
    while wizard.health > 0 and player.health > 0:
        turn_end = False
        while turn_end == False:
            print("\n--- Your Turn ---")
            print("1. Attack")
            print("2. Use Special Ability")
            print("3. Use Defensive Ability")
            print("4. Heal")
            print("5. View Stats")

            choice = input("Choose an action: ")

            if choice == '1':
                player.attack(wizard)
                turn_end = True
            elif choice == '2':
                player.special_attack(wizard)
                turn_end = player.special_attack(wizard)
            elif choice == '3':
                player.defensive_special_ability()
                turn_end = True
            elif choice == '4':
                player.heal()
                turn_end = True
            elif choice == '5':
                player.display_stats()
                wizard.display_stats()
            else:
                print("Invalid choice. Try again.")
            
            if player.special_attack_cooldown > 0:
                player.special_attack_cooldown-=1
                print(f"Special move is ready in {player.special_attack_cooldown} turn(s)!")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print("\n-----------------")
        print("VICTORY!")
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("Gorlock")
    battle(player, wizard)

if __name__ == "__main__":
    main()