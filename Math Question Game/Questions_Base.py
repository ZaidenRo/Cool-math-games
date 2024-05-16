##############################
#Prog:Cool Math Games        #
#Purpose:To make a quiz game #
#Author:zaidenroets@gmail.com#
#Date:14/05/2024             #
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
      if response == "yes" or response == "y":
          return "yes"
      elif response == "no" or response == "n":
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


def question_amount(how_many):
    # Checks the amount of questions the user would like to answer
    how_many = int(input(how_many))
    # Makes sure the user chose a number between 1 and 10
    if how_many < 1 or how_many > 10:
        print("Please enter a number from 1-10 which does not have a decimal point:")

# Asks the user how many questions they would like to answer
amount = question_amount('How many questions would you like to answer, please chose a number from 1 - 10:')

# Asks the user how hard the difficulty they want to be ( easy, normal, hard)
def question_difficulty(difficulty):
    diff = input(difficulty).lower()
    if diff == 'easy':
        print('You have chosen easy difficulty')
    elif diff == 'normal':
        print('You have chosen normal difficulty')
    elif diff == 'hard':
        print('You have chosen hard difficulty')
    else:
        print("Please chose easy, normal or hard")

# Input for game difficulty
chosen_diff = question_difficulty('''Please chose a difficulty.
Easy
Normal
Hard
Chose:''')
