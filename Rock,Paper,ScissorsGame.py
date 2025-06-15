#Rock, Paper, Scissors Game
import random 
def get_computer_choice():
    choices = ['rock','paper','scissors']
    return random.choice(choices)
def grt_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice
def determine_winner(user_choice, computer_choice):
    print(f"\nnyou chose: {user_choice} ")
    print(f"computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice =='scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors'and computer_choice == 'paper'):
        return "younwin!"
    else:
        return "computer wins!"
    
def play_game():
    print("wlcome to rock, paper, scissors!")
    user_choice = grt_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()



