import random
import datetime

##############################
# Prog:Cool Math Games        #
# Purpose:To make a quiz game for teachers to use at school #
# Author:zaiden.roets@papamoacollege.school.nz#
# Date:14/05/2024             #
##############################

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

        # checks user response, question
        # repeats if users don't enter yes / no
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
            how_many = int(input('How many questions would you like to answer, please chose a number from 1 - 20: '))
            # Makes sure the user chose a number between 1 and 10
            if 1 <= how_many <= 20:
                return how_many
            else:
                print("Please enter a number from 1-20 which does not have a decimal point:")
        # Checks if they have input an error such as <enter>
        except ValueError:
            print("That's not a valid number, please try again.")

# Asks the user how many questions they would like to answer
amount = question_amount()

# Asks the user how hard the difficulty they want to be ( easy, normal, hard)
def question_difficulty(difficulty):
    while True:
        # Puts all input in lowercase
        diff = input(difficulty).lower()
        # Easy will have really easy questions fit for a year 8-9 level
        if diff == 'easy':
            difficulty_level = 'easy'
            print('You have chosen easy difficulty')
            return difficulty_level
        # Normal will have questions fit for a year 10-11 level
        elif diff == 'normal':
            difficulty_level = 'normal'
            print('You have chosen normal difficulty')
            return difficulty_level
        # Hard will have questions fit for a year 12-13 level
        elif diff == 'hard':
            difficulty_level = 'hard'
            print('You have chosen hard difficulty')
            return difficulty_level
        # Makes sure they input the right game mode
        else:
            print("Please choose easy, normal or hard")

# Input for game difficulty
chosen_diff = question_difficulty('''Please choose a difficulty.
Easy
Normal
Hard
Choose: ''')

def askNum():
    while True:
        try:
            userInput = int(input("Enter a number: "))
            return userInput
        # Making sure the user only inputs a number
        except ValueError:
            print("Incorrect Input!")

def askQuestion():
    # Generate random numbers based on difficulty level
    if chosen_diff == 'easy':
        x = random.randint(1, 10)
        y = random.randint(1, 10)
    elif chosen_diff == 'normal':
        x = random.randint(1, 100)
        y = random.randint(1, 100)
    elif chosen_diff == 'hard':
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
 #Asks the math question
    print(f"What is {x} x {y}?")

    user_answer = askNum()
# Does the math for the questions
    if user_answer == x * y:
        print("Correct!")
        return 1
    else:
        print("Incorrect! The correct answer is", x * y)
        return 0

# Adds a point if the user gets the answer correct
correct = 0
for _ in range(amount):
    correct += askQuestion()

print(f"You got {correct} correct out of {amount}")

# Displays the player their results
def player_result(result):
    while True:
        results = input(result).lower()

    # checks user response, question
    # repeats if users don't enter yes / no
        if results in ["yes", "y"]:
            return "yes"
        elif results in ["no", "n"]:
            return "no"
        else:
            print('Please enter yes / no')

printed_result = player_result("Would you like to see your results?")
if printed_result == 'yes':
    # Shows the user their percent of questions they got correct
    print("You got",correct/amount*100,"% correct")
elif printed_result == 'no':
    print('Thank you for playing!')
    quit()
