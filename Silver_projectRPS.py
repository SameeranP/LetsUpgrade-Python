import random


def player_choice(user_choice):  # Register and shows the players choice
    if user_choice == 1:
        print("The player chose rock")
    elif user_choice == 2:
        print("The player chose paper")
    else:
        print("The player chose scissors")

def computer_choice(cpu_choice):  # Register and shows the cpus choice
    if cpu_choice == 1:
        print("The computer chose rock")
    elif cpu_choice == 2:
        print("The computer chose paper")
    else:
        print("The computer chose scissors")


def result(user_choice, cpu_choice, player_score, cpu_score,t):  # Define the game result
    if user_choice == cpu_choice:
        return [player_score, cpu_score, t +1]
    elif user_choice == 1 and cpu_choice == 3:
        return [player_score + 1, cpu_score, t]
    elif user_choice == 2 and cpu_choice == 1:
        return [player_score + 1, cpu_score, t]
    elif user_choice == 3 and cpu_choice == 2:
        return [player_score + 1, cpu_score, t]
    else:
        return [player_score, cpu_score + 1, t]


def print_score(p_score, c_score,t):  # Identifies the result and print the total score
    print("Score:""\nPlayer:", p_score, "\nComputer:", c_score, "\nTies:",t)


def validation_input():  # Validates the input
    while True:
        try:
            user_input = int(input("Put your choice:"))
            if user_input not in range(1, 4):
                print("We only accept commands between 1 and 3, according to the table, type again")
                continue
            if type(user_input) == int:
                break
        except ValueError:
            print("We only accept exact numbers")
            continue
    return user_input


print('''1 - Rock
2 - Paper
3 - Scissors''')  # Printing the instructions
human_score = 0
computer_score = 0
ties = 0
while True:  # The condition is not important since the loop will stop on line 68 if the user wishes so
    user = validation_input()
    player_choice(user)
    ai = random.randint(1, 3)
    computer_choice(ai)
    human_score, computer_score, ties= result(user, ai, human_score, computer_score,ties)  # Accumulate the score
    print_score(human_score, computer_score,ties)
    command = int(input("Type 0 to stop the program, type any another number to keep playing"))
    if command == 0:
        break
