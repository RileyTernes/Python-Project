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
    #displays a menu, 1. Start New Game, 2. Choose Range, 3. Exit.
    #function returns fallowing functions based upon function chosen.
    
    print("Choose option by typing in number")
    number = input(f"1. Start New Game \n 2.Choose range \n 3. Exit")
    if number == 1:
        selection = name
    if number == 2:
        selection = random_integer
    
    #displays a menu
    return selection
def name():
    player1 = input("Please enter the first player's name: ")
    player2 = input("Please enter the second player's name: ")
    return player1, player2
def random_integer(range_low, range_high):
    random_number = random.randint(range_low, range_high)
def take_turns(random_number, player1, player2):
    #Takes variables random_number and players.
    #Takes turns asking between 2 user to guess the random number
    #Tells wether the number is to high or to low
    #Returns who the winner is.
    player1_guess = x
    player2_guess = x
    
    while player1_guess or player2_guess != random_number: #repeats guessing process until random number is guessed
        player1_guess = int(input(f"{player1}, enter your guess")) #askes player 1 to their guess
        if player1_guess > random_number: #if statements used to state if number is higher or lower, if number is guessed than program ends
            print("lower")
        if player1_guess < random_number:
            print("higher")
        if player1_guess == random_number:
            print(f"{player1} wins!")
            exit()
        player2_guess = int(input(f"{player2}, enter your guess")) #same thing as previous staetment
        if player2_guess > random_number:
            print("lower")
        if player2_guess < random_number:
            print("higher")
        if player2_guess == random_number:
            print(f"{player2} wins!")
            exit()
        
