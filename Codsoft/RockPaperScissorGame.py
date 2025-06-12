#Rock-Paper-Scissors Game
#Name : Shubham Lade
#Description : Rock-Paper-Scissors Game. User Input, Computer Selection, Game logic, Display Result, Score Tracking,
#               play again, user interface

import random

def get_user_choice():
    print("\nChoose one of the following: rock, paper or scissors")
    user_input = input("Your choice: ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input: Please choose rock, paper or scissors.")
        user_input = input("Your choice: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "user"
    else:
        return "computer"
    
def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if winner == "Tie":
        print("Result: It's a Tie!")
    elif winner == "user":
        print("Result: You win! :)")
    else: 
        print("Result: You lose! :(")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("-----Welcome to Rock-Paper-Scissors Game-----")

    while True:
        print(f"\n-----Round {round_number}-----")
        user = get_user_choice()
        computer = get_computer_choice()
        winner = determine_winner(user, computer)

        display_result(user, computer, winner)

        if winner == "user":
            user_score +=1
        elif winner == "computer":
            computer_score +=1

        print(f"Current Score -> Your: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again not in ['yes']:
            print("\n ---Final Score---")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        round_number +=1

if __name__ == "__main__":
    play_game()