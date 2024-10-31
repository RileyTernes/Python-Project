#Number Guessing Game
def main():
    #calls all of the functions
    #drives program
    #recieves no arguments
    menu()
    name()
    random_integer(range)
    
    
def menu():
    #displays a menu, 1. Start New Game, 2. Choose Range, 3. Exit.
    #function returns fallowing functions based upon function chosen.
    
    print("Choose option by typing in number")
    number = input(f"1. Start New Game \n 2.Choose range \n 3. Exit")
    if number == 1:
        selection = name
    if number == 2:
        selection = random_integer
    
    return selection
def name():
    
def random_integer(range):
    
    
def take_turns():