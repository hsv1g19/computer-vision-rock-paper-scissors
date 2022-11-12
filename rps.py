import random
import time

import cv2
import numpy as np
from keras.models import load_model


class rock_paper_scissors():

    def __init__(self):
        """This method lets the class initializes the object's(rock paper scissors) attributes including the dowloaded model, video capture, 
           options for rock, papaer scissors or nothing, computer wins, user wins and rounds played.
        """

        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.options = ['rock', "paper", "scissors", "nothing"]
        self.computer_wins = 0
        self.user_wins = 0
        self.rounds_played = 0
    
    
  
    def get_prediction(self):
        """ 
        This method gets the prediction from the model which is the highest probability of choosing
        either rock paper or scissors.

        Returns
        -------
        Integer 
            _returns the highest index in the array
        """
        predictions = self.model.predict(self.data)
        max_val_index = np.argmax(predictions)
        return max_val_index


    def get_computer_choice(self):
        """Using random.choice function the computer randomly picks from the list of options from the first element
           up to the 3rd element, not including the 4th.
        """
        self.computer_choice = random.choice(self.options[0:3])
        
    def get_user_choice(self):
        """ 
        Using the output of the previous function get prediction, this function indexes the list of options with the max index
        and gets the corresponding value from the options list
        """
        max_val_index = self. get_prediction()
        if max_val_index == 3:   #if max index is nothing (the 3rd index)
            self.user_choice = 'None'
        else:
            self.user_choice = self.options[max_val_index]
            print(f'You chose {self.user_choice}')
            print(f'The computer chose {self.computer_choice}')


    def get_winner(self):

        """Using if-elif-else statements, the script chooses a winner based on the classic rules of Rock-Paper-Scissors
           it also adds a counter one to both rounds played, computer wins and user wins, depending on who won the particular round.
        """
        if self.user_choice == self.computer_choice:
            self.winner= "Both players selected the same. It's a tie!"
            self.rounds_played+=1
        elif self.user_choice == "rock":
            if self.computer_choice == "scissors":
                self.winner= "Rock smashes scissors! You win!"
                self.rounds_played+=1
                self.user_wins+=1
            else:
                self.winner= "Paper covers rock! You lose computer won."
                self.rounds_played+=1
                self.computer_wins+=1
        elif self.user_choice == "paper":
            if self.computer_choice == "rock":
                self.winner= "Paper covers rock! You win!"
                self.rounds_played+=1
                self.user_wins+=1
            else:
                self.winner = "Scissors cuts paper! You lose computer won."
                self.rounds_played+=1
                self.computer_wins+=1
        elif self.user_choice == "scissors":
            if self.computer_choice == "paper":
                self.winner="Scissors cuts paper! You win!"
                self.rounds_played+=1
                self.user_wins+=1
            else:
                self.winner="Rock smashes scissors! You lose computer won."
                self.rounds_played+=1
                self.computer_wins+=1
        
    def get_game_winner(self):

        """ This function returns the winner of the entire game by comparing the computer wins with user wins
        """
        if self.computer_wins > self.user_wins :
            print("You lost, the computer won")
        elif self.user_wins > self.computer_wins:
            print("You won! ")
        
        
    def play_game(self):
        """ The play game incorporates many of the previous functions 
        """

        print('''Welcome to the rock papers scissors game!, 
            you will see the instructions on the screen when the camara is on. After the word Go cue
            show your choice. Good luck!''')

        while True:
            
            timer = 3 #initialises timer for countdown
            
            """
            lines (120-126) opens the user camera, displays instructions for running &
            stopping the game and starts acquiring frames
            """

            self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            ret, frame = self.cap.read()
            font = cv2.FONT_HERSHEY_DUPLEX  
            cv2.putText(frame, 'Press the c key to start countdown', (0, 50), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, 'Press the q key to stop game', (0, 100), font, 1, (225, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow('frame', frame)
            cv2.waitKey(1)

            
            if cv2.waitKey(80) & 0xFF == ord('c'): #if user press c countdown starts
                
                start_time=time.time()#returns time at the start of countdown

                while timer > 0: # if timer > 0  the timer is displayed on screen 
                    font = cv2.FONT_HERSHEY_DUPLEX 
                    ret, frame = self.cap.read()
                    cv2.putText(frame, str(timer), (224, 224), font, 6, (255, 0, 0), 4, cv2.LINE_AA)
                    cv2.imshow('frame', frame)
                    cv2.waitKey(5)# the timer will appear for 5 milliseconds before it moves on
                    current_time = time.time()
                    if current_time - start_time >= 1:
                        start_time = current_time 
                        timer-=1 #decrease timer down by 1 second
                        
                else:  #if timer is equal to zero show Start! on the screen
                         
                    ret, frame = self.cap.read()
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, 'Start!', (50, 250), font, 5, (255, 145, 0), 4, cv2.LINE_AA)
                    cv2.imshow('frame', frame) # show start on the screen
                    cv2.waitKey(10) # wait 10 milliseconds before start dissapears
                    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                    image_np = np.array(resized_frame)
                    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                    self.data[0] = normalized_image
                    cv2.imshow('frame', frame) 
                    
                    
                    self.get_computer_choice()# once timer is zero the function will get user and computer choice and round winner
                    self.get_user_choice()
                    self.get_winner()
                    
                    
                    if self.rounds_played == 3:
                        self.get_game_winner() # call this function to get the winner of the whole game if rounds played equals 3
                        self.cap.release()#Closes video file or capturing device/camera
                        print(f'You played 3 rounds, the game is finished.')
                        break

            elif cv2.waitKey(80) & 0xFF == ord('q'): #if user press q camera and game stops
                print(f'You left game before 3 rounds')
                break
        
            else:  #reinitialise timer back to 3s - to prepare for another round
                timer = 3


if __name__ == '__main__':
    # call the play game function

    game = rock_paper_scissors()
    game.play_game()
   


