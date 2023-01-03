# Computer Vision RPS

![rockpaperscissors](https://user-images.githubusercontent.com/117317215/210436893-92b24dfb-6d91-48db-a220-c8c86b73a1a0.jpg)

Project Documentation
This project uses the web application TeachableMachine to train a deep learning model to recognise whether the user is displaying to the webcam rock, paper, or scissors, and executes the logic for a best-of-three game between user and computer.

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

This projects implements the Rock-Paper-Scissors game, where the user plays with the computer using computer vision.

A webcam window will appear on a three second timer, to which the user shows a hand gesture representing rock, paper, or scissors. The game will continue until either the user or the computer has won three rounds.

### Milestone 1: Creation of the Computer Vision System
Technologies / Skills:

Teachable Machine
Web application Teachable Machine is used for creating machine learning models based on image or audio files. A model to recognise the three classes of the game (Rock, Paper, and Scissors), as well as a 'Nothing' class, was trained and imported. The model is contained in the keras_model.h5 file, with the class labels shown in the labels.txt file.


### Milestone_2
Using Teachable Machines, I have created an image project model with four classes: Rock, Paper, Scissors and None. In a future milestone, I will use this model to receive user input from the camera.

### Milestone 3: Create a Rock-Paper-Scissors Game

Manual version of the rock-paper-scissors game created in the python file manual_rps.py. The get_computer_input function randomly chooses "rock", "paper", or "scissors", the get_user_input function asks the user for a choice from the same options, and the get_winner functions returns the winner according to the rules of the game. The play function runs the game as expected by calling the previous three functions sequentially. This game is contained in the manual_rps.py file.


### Milestone_4 - manual_rps.py
The manual_rps.py file contains the code to play the rock paper scissors game, with the user typing "rock", "paper" or "scissors". The computer chooses one of the words at random. The user-selected word is compared with the computer-selected word to determine whether the user or computer has won the game.

Technologies / Skills:

opencv-python
keras
mediapipe
The get_user_input function from the manual game is replaced by a get_prediction function which uses keras as an interface for the TensorFlow library to predict whether the user is displaying rock, paper, or scissors in the camera.

