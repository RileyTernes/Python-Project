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
        
    current_player = player1
    total = 0
    guess = int(input("Enter a number between ",range_low," - "range_high": "))
    total += 1
    while guess > range_high or guess < range_low:
        print("That number is not within the range. The range is ",range_low," - ",range_high". Try again.")
        guess_player1 = int(input(f"{current_player}, please enter a number between ",range_low," - "range_high": "))
    if guess > random_number:
        print("That guess was too high.")
    if total % 2 == 0:
        current_player = player1
    else:
        current_player = player2
    elif guess < random_number:
        print("That guess was too low.")
    elif:
        print("That guess was correct! ",current_player," guessed the number in "total" guesses! Congratulations!")
        quit()
    
def range_getter():
    range_low == int(input("Please enter the floor for the range: "))
    range_high == int(input("Please enter the ceiling for the range: "))
    return range_low, range_high