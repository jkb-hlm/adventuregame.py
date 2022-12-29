import time
import random

monster = random.choice(["dragon", "gorgon", "wicked fairie"])
protagonist = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monster} is somewhere around here,")
    print_pause("and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def approach_house():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens "
                "and out steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    action_house = input("Would you like to (1) fight or (2) run away?")
    if action_house == "1":
        fight()
    if action_house == "2":
        flea()
    else:
        basic_decision()


def fight():
    if "sword" in protagonist:
        print_pause(f"the {monster} sees the sword and goes back "
                    "inside. You won.")
        play_again()
    else:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        print_pause("you gave it all, but lost.")
        play_again()


def flea():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")
    basic_decision()


def peer_cave():
    if "sword" in protagonist:
        print_pause("You have been here before.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and "
                    "take the sword with you.")
        protagonist.append("sword")
    print_pause("You walk back out to the field.")
    basic_decision()


def basic_decision():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1 or 2.)")
    if choice == '1':
        approach_house()
    if choice == '2':
        peer_cave()
    else:
        basic_decision()


def play_again():
    input("Would you like to play again? (y/n)")
    if input == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    if input == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    intro()
    basic_decision()


play_game()
