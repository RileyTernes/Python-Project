#Number Guessing Game
import random
def main():
    #set default range
    range_low = 1
    range_high = 1000
    #calls all of the functions
    #drives program
    #recieves no arguments
    menu()
    if selection == "start":
        name()
        random_integer(range_low)
        take_turns(random_number, player1, player2)
    if selection == "range":
        
    
def menu():
    #displays a menu, 1. Start New Game, 2. Choose Range, 3. Exit.
    #function returns fallowing functions based upon function chosen.
    
    print("Choose option by typing in number")
    number = input(f"1. Start New Game \n 2.Choose range \n 3. Exit")
    if number == 1:
        selection = "start"
    if number == 2:
        selection = "range"
    else:
        quit()
    #displays a menu
    return selection
def name():
    player1 = input("Please enter the first player's name: ")
    player2 = input("Please enter the second player's name: ")
    return player1, player2
def random_integer(range_low, range_high):
    random_number = random.randint(range_low, range_high)
def take_turns(random_number, player1, player2):

def range_getter():
    range_low == int(input("Please enter the floor for the range: "))
    range_high == int(input(Please enter the ceiling for the range: "))
