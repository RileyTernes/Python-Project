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
    player1 = string(input("Please enter the first player's name: "))
    player2 = string(input("Please enter the second player's name: "))
    return player1, player2
def random_integer(range_low, range_high):
    random_number = random.randint(range_low, range_high)
def take_turns(random_number, player1, player2):
<<<<<<< HEAD
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
