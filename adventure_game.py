import time
import random
enemy = ["dragon", "gorgon", "pirate", "wicked"]
face_enemy = random.choice(enemy)
path = []


def play_game():
    intro()


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")
    field()


def print_pause(ask):
    print(ask)
    time.sleep(2)


def fight():
    if "ogoroth" in path:
        print_pause(f"As the {face_enemy} moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause(f"But the {face_enemy} takes one look at "
                    "your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {face_enemy}. "
                    "You are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {face_enemy}.")
        print_pause("You have been defeated!")
        play_again()


def play_again():
    more = input("Would you like to play again? (y/n)").lower()
    while True:
        if more == "n":
            print_pause("ok, bye!")
            exit()
        elif more == "y":
            global face_enemy
            face_enemy = random.choice(enemy)
            global path
            path = []
            play_game()
            break
        else:
            play_again()


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice()


def choice():
    answer = input("(Plz enter 1 or 2.)")
    while True:
        if "1" == answer:
            house()
            break
        elif "2" == answer:
            cave()
            break
        else:
            choice()


def cave():
    if "ogoroth" in path:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.")
        path.append("ogoroth")
        field()


def house():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and "
                "out steps a {face_enemy}.")
    print_pause(f"Eep! This is the {face_enemy}'s house!")
    print_pause(f"The {face_enemy} attacks you!")
    print_pause("You feel a bit under-prepared for this, "
                "what with only having a tiny dagger.")
    housechoice = input("Would you like to (1) fight or (2) run away?")
    if "1" == housechoice:
        fight()
    elif "2" == housechoice:
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
        field()


play_game()
