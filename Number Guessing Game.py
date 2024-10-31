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
    player1 = string(input("Please enter the first player's name: "))
    player2 = string(input("Please enter the second player's name: "))
    return player1, player2
def random_integer(range_low, range_high):
    random_number = random.randint(range_low, range_high)
def take_turns(random_number, player1, player2):
    current_player = player1
    total = 0
    guess = int(input("Enter a number between ",range_low," - "range_high": "))
    total += 1
    while guess > range_high or guess < range_low:
        print("That number is not within the range. The range is ",range_low," - ",range_high". Try again.")
        guess_player1 = int(input(f"{current_player}, please enter a number between ",range_low," - "range_high": "))
    if guess > random_number:
        print("That guess was too high.")
        if total = 
    elif guess < random_number:
        print("That guess was too low.")
    elif:
        print("That guess was correct! ",current_player," guessed the number in "total" guesses! Congratulations!")
        quit()
    