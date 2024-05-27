import random


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
def play_game():
    # Function to prompt yes/no questions
    def yes_no(question):
        while True:
            response = input(question).lower()
            if response in ["yes", "y"]:
                return "yes"
            elif response in ["no", "n"]:
                return "no"
            else:
                print('Please enter yes / no')

    # Function to display instructions
    def instruction():
        print('''In this math game you will be challenged on your statistics knowledge.
        You will be asked how many questions you want to answer, it ranges from 1-10 mathematical questions.
        You will have the option to see your overall results after you have completed the questions.''')

    # Display instructions if requested
    want_instructions = yes_no('Do you want to read the instructions?:')
    if want_instructions == "yes":
        instruction()

    # Function to get the number of questions from the user
    def question_amount():
        while True:
            try:
                how_many = int(input('How many questions would you like to answer, please choose a number from 1 - 20: '))
                if 1 <= how_many <= 20:
                    return how_many
                else:
                    print("Please enter a number from 1-20 which does not have a decimal point:")
            except ValueError:
                print("That's not a valid number, please try again.")

    amount = question_amount()

    # Function to prompt for the game difficulty
    def question_difficulty(difficulty):
        while True:
            diff = input(difficulty).lower()
            if diff in ['easy', 'normal', 'hard']:
                print(f'You have chosen {diff} difficulty')
                return diff
            else:
                print("Please choose easy, normal or hard")

    chosen_diff = question_difficulty('''Please choose a difficulty.
    Easy
    Normal
    Hard
    Choose: ''')

    # Function to ask the user for input number
    def ask_num():
        while True:
            try:
                user_input = int(input("Enter a number: "))
                return user_input
            except ValueError:
                print("Incorrect Input!")

    # Function to ask a multiplication question
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
            return (1, f"{x} x {y} = {x*y}")
        else:
            print(f"Incorrect! The correct answer is {x * y}")
            return (0, f"{x} x {y} = {x*y}")

    results_history = []  # Store history of questions and answers

    correct = 0
    # Loop through each question
    for _ in range(amount):
        result, question = ask_question()
        results_history.append((question, "Correct" if result else "Incorrect"))
        correct += result

    # Display the number of correct answers
    print(f"You got {correct} correct out of {amount}")

    # Function to prompt whether to see results or not
    def player_result(result):
        while True:
            results = input(result).lower()
            if results in ["yes", "y"]:
                return "yes"
            elif results in ["no", "n"]:
                return "no"
            else:
                print('Please enter yes / no')

    # Display results if requested
    printed_result = player_result("Would you like to see your results?")
    if printed_result == 'yes':
        print(f"You got {correct / amount * 100}% correct")
        print("Results History:")
        for question, result in results_history:
            print(f"{result}: {question}")
    elif printed_result == 'no':
        print('Thank you for playing!')

# Function to ask if user wants to play again
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
