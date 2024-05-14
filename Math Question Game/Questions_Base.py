##############################
#Prog:Cool Math Games        #
#Purpose:To make a quiz game #
#Author:zaidenroets@gmail.com#
#Date:14/05/2024             #
##############################



import random
# Welcomes the user
print("⚡️⚡️⚡️Welcome to Cool Math Games⚡️⚡️⚡️")


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

# Asks the user if they would like to see the instrctions.
want_instructions = yes_no('Do you want to read the instructions?')

# Checks if user enters yes(y) or no (n)
if want_instructions == "yes":
  instruction()


def question_amount(how_many):
    # Checks the amount of questions the user would like to answer
    amount = input(how_many)
    if how_many == <10 or how_many == >1:
        print("Please chose a number from 1-10")


