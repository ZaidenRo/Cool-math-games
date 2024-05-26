import random
import datetime


##############################
# Prog:Cool Math Games        #
# Purpose:To make a quiz game for teachers to use at school #
# Author:zaiden.roets@papamoacollege.school.nz#
# Date:14/05/2024             #
##############################

def play_game():
    # Welcomes the user
    print('''
    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ░█████╗░░█████╗░░█████╗░██╗░░░░░
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║░░░░░
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██║░░╚═╝██║░░██║██║░░██║██║░░░░░
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║░░██╗██║░░██║██║░░██║██║░░░░░
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ╚█████╔╝╚█████╔╝╚█████╔╝███████╗
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ░╚════╝░░╚════╝░░╚════╝░╚══════╝

    ███╗░░░███╗░█████╗░████████╗██╗░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗░██████╗
    ████╗░████║██╔══██╗╚══██╔══╝██║░░██║  ██╔════╝░██╔══██╗████╗░████║██╔════╝██╔════╝
    ██╔████╔██║███████║░░░██║░░░███████║  ██║░░██╗░███████║██╔████╔██║█████╗░░╚█████╗░
    ██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗
    ██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝
    ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░️''')

    # Checks if user enters yes(y) or no (n)
    def yes_no(question):
        while True:
            response = input(question).lower()
            if response in ["yes", "y"]:
                return "yes"
            elif response in ["no", "n"]:
                return "no"
            else:
                print('Please enter yes / no')

    # Instructions for the game
    def instruction():
        print('''In this math game you will be challenged on your statistics knowledge.
        You will be asked how many questions you want to answer, it ranges from 1-10 mathematical questions.
        You will have the option to see your overall results after you have completed the questions.''')

    # Asks the user if they would like to see the instructions.
    want_instructions = yes_no('Do you want to read the instructions?:')

    # Checks if user enters yes(y) or no (n)
    if want_instructions == "yes":
        instruction()

    def question_amount():
        # Asks the user how many questions they would like to answer
        while True:
            try:
                how_many = int(
                    input('How many questions would you like to answer, please choose a number from 1 - 20: '))
                # Makes sure the user chose a number between 1 and 20
                if 1 <= how_many <= 20:
                    return how_many
                else:
                    print("Please enter a number from 1-20 which does not have a decimal point:")
            except ValueError:
                print("That's not a valid number, please try again.")

    # Asks the user how many questions they would like to answer
    amount = question_amount()

    # Asks the user how hard the difficulty they want to be (easy, normal, hard)
    def question_difficulty(difficulty):
        while True:
            diff = input(difficulty).lower()
            if diff in ['easy', 'normal', 'hard']:
                print(f'You have chosen {diff} difficulty')
                return diff
            else:
                print("Please choose easy, normal or hard")

    # Input for game difficulty
    chosen_diff = question_difficulty('''Please choose a difficulty.
    Easy
    Normal
    Hard
    Choose: ''')

    def ask_num():
        while True:
            try:
                user_input = int(input("Enter a number: "))
                return user_input
            except ValueError:
                print("Incorrect Input!")

    def ask_question():
        if chosen_diff == 'easy':
            x = random.randint(1, 10)
            y = random.randint(1, 10)
        elif chosen_diff == 'normal':
            x = random.randint(1, 100)
            y = random.randint(1, 100)
        elif chosen_diff == 'hard':
            x = random.randint(1, 1000)
            y = random.randint(1, 1000)

        print(f"What is {x} x {y}?")
        user_answer = ask_num()
        if user_answer == x * y:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect! The correct answer is {x * y}")
            return 0

    correct = 0
    for _ in range(amount):
        correct += ask_question()

    print(f"You got {correct} correct out of {amount}")

    def player_result(result):
        while True:
            results = input(result).lower()
            if results in ["yes", "y"]:
                return "yes"
            elif results in ["no", "n"]:
                return "no"
            else:
                print('Please enter yes / no')

    printed_result = player_result("Would you like to see your results?")
    if printed_result == 'yes':
        print(f"You got {correct / amount * 100}% correct")
    elif printed_result == 'no':
        print('Thank you for playing!')


def play_again():
    while True:
        answer = input('Do you want to play again? ').lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print('Please enter yes / no')


# Main loop to start and potentially restart the game
while True:
    play_game()
    if not play_again():
        print('Thank you for playing!')
        break
