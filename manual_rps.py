import random

word_list = ["rock", "paper", "scissors"]

def get_computer_choice(self):
    self.computer_choice = random.choice(word_list)
    return computer_choice


def get_user_choice():
    user_choice = input("Rock, Paper, Scissors: ").lower()
    return user_choice

def get_winner(computer_choice, user_choice):
    #self.computer_choice = computer_choice
    #self.user_choice = user_choice
    
    if computer_choice == user_choice:
        print('It is a tie!')
    elif (
        (computer_choice == 'rock' and user_choice == 'scissors') or
        (computer_choice == 'paper' and user_choice == 'rock') or
        computer_choice == 'scissors' and user_choice == 'paper'
        ):
        print('You lost!')
    else:
        print('You won!')

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)


play()
