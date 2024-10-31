#Number Guessing Game
import random
def main():
    #calls all of the functions
    #drives program
    #recieves no arguments
    menu()
    name()
    random_integer(range_low, range_high)
    take_turns(random_number, player1, player2)
    
def menu():
    #displays a menu
    return selection
def name():
    player1 = input("Please enter the first player's name: ")
    player2 = input("Please enter the second player's name: ")
    return player1, player2
def random_integer(range_low, range_high):
    random_number = random.randint(range_low, range_high)
def take_turns(random_number, player1, player2):
    asd