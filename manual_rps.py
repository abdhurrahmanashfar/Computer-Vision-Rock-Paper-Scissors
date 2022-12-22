import random

#word_list = ["rock", "paper", "scissors"]

def get_computer_choice():
    word_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(word_list)
    return computer_choice


def get_user_choice():
    user_choice = input("Rock, Paper, Scissors: ").lower()
    return user_choice
