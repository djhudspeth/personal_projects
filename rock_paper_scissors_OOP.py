import random

def user_pick():

    while True:
        game_options = [1,2,3]
        
        user_choice = input("\nWhat do you chose? Type 1 for Rock, 2 for Paper or 3 for Scissors. ")

        if user_choice.isdigit() == True:
            user_digit = int(user_choice)
            if user_digit in game_options:
                if user_digit == 1:
                    user_choice = 'Rock'
                if user_digit == 2:
                    user_choice = 'Paper'
                if user_digit == 3:
                    user_choice = 'Scissors'

                return user_choice

            else:
                continue    
            

def computer_pick():

    computer_choice = random.randint(1,3)

    if computer_choice == 1:
        computer_choice = 'Rock'
    if computer_choice == 2:
        computer_choice = 'Paper'
    if computer_choice == 3:
        computer_choice = 'Scissors'

    return computer_choice

def play_game():

    user_choice = user_pick()
    computer_choice = computer_pick() 

    print(f"\nUser selects: {user_choice}\nComputer selects: {computer_choice}")

    if user_choice == computer_choice:
        print("\nIts a tie!\n")

    if user_choice == 'Rock' and computer_choice == 'Scissors':
        print("\nRock beats Scissors...You Win!\n")
    if user_choice == 'Paper' and computer_choice == 'Rock':
        print("\nPaper beats Rock...You Win!\n")
    if user_choice == 'Scissors' and computer_choice == 'Paper':
        print("\nScissors beats Paper...You Win!\n")

    if user_choice == 'Rock' and computer_choice == 'Paper':
        print("\nPaper beats Rock...You Lose...\n")
    if user_choice == 'Paper' and computer_choice == 'Scissors':
        print("\nScissors beats Paper...You Lose...\n")
    if user_choice == 'Scissors' and computer_choice == 'Rock':
        print("\nRock beats Scissors...You Lose...\n")


play = True
while play:
    play_game()
    again = input("Play again? 'y' for yes or 'q' to quit: ")
    if again == 'q':
        play = False
