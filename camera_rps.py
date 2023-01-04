import cv2
from keras.models import load_model
import numpy as np
import time
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

choices = ["rock", "paper", "scissors", "nothing"]

def get_computer_choice():
    computer_choice = random.choice(choices[0:3])
    return computer_choice


def get_prediction():
    #model = load_model('keras_model.h5')
    #cap = cv2.VideoCapture(0)
    #data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    time_1 = time.time()

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        max_index = np.argmax(prediction[0])
        user_choice = choices[max_index]
        
    return user_choice

        
    # After the loop release the cap object
    #cap.release()
    # Destroy all the windows
    #cv2.destroyAllWindows()



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
    
    computer_wins = 0
    user_wins = 0
    
    while computer_wins < 3 and user_wins < 3:
        computer_choice = get_computer_choice()
        user_choice = get_prediction()
        overall_winner = get_winner(computer_choice, user_choice)  
        #print(f'overall_winner variable = {overall_winner}')
        if overall_winner == 'computer':
            computer_wins += 1
        elif overall_winner == 'user':
            user_wins += 1
        else:
            print("No change to the score... Have another go.")
        
        print(f'Computer: {computer_wins} User: {user_wins}\n')
        
    if computer_wins == 3:
        print(f'FINAL SCORE is Computer: {computer_wins} User: {user_wins}\n')
        print("Sorry, you didn't win")
        
    elif user_wins == 3:
        print(f'FINAL SCORE is Computer: {computer_wins} User: {user_wins}\n')
        print("You won!")
            
    else:
        print('Something went wrong')
            
      # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

play()
