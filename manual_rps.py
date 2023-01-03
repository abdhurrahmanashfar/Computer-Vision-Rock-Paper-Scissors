import random

#word_list = ["rock", "paper", "scissors"]

def get_computer_choice():
    word_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(word_list)
    return computer_choice


def get_user_choice():
    user_choice = input("Rock, Paper, Scissors: ")
    return user_choice

def get_winner(computer_choice, user_choice):
    #self.computer_choice = computer_choice
    #self.user_choice = user_choice
    
    if computer_choice == user_choice:
        print('It is a tie!')
    elif (
        (computer_choice == 'Rock' and user_choice == 'Scissors') or
        (computer_choice == 'Paper' and user_choice == 'Rock') or
        computer_choice == 'Scissors' and user_choice == 'Paper'
        ):
        print('You lost!')
    else:
        print('You won!')

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)


play()
