import random
import cv2
import time
from keras.models import load_model
import numpy as np




class rock_paper_scissors():

    def __init__(self):

        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.options = ['rock', "paper", "scissors", "nothing"]
        self.computer_wins = 0
        self.user_wins = 0
        self.rounds_played = 0
    
    
  
    
    def get_prediction(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """

       

        predictions = self.model.predict(self.data)
        max_val_index = np.argmax(predictions[0])
        return max_val_index


    def get_computer_choice(self):
        self.computer_choice = random.choice(self.options)
        print(f'The computer chose {self.computer_choice}')

    def get_user_choice(self):
        self.user_choice = self.options[self.get_prediction]
        
        # if max_val_index ==0:
        #     choice='rock'
        # if max_val_index ==1:
        #    choice='paper'
        # if max_val_index == 2:
        #     choice='scissors'
        # if max_val_index == 3:
        #     choice = 'nothing'
        # return print(f"You chose {choice}")
        print(f'You chose {self.user_choice}')


    def get_winner(self):
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
        if self.computer_wins > self.user_wins :
            print("You lost, the computer won")
        elif self.user_wins > self.computer_wins:
            print("You won! ")
        
        
    def play_game(self):

        print('''Welcome to the rock papers scissors game!, 
            you will see the instructions on the screen when the camara is on. After the word Go cue
            show your choice. Good luck!''')

            
        while True:
            timer = 3

            self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            ret, frame = self.cap.read()
            font = cv2.FONT_HERSHEY_DUPLEX  
            cv2.putText(frame, 'Press the c key to start countdown', (0, 50), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, 'Press the q key to stop game', (0, 100), font, 1, (225, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow('frame', frame)

            if cv2.waitKey(10) & 0xFF == ord('c'):
                start_time=time.time()

                while timer > 0:
                    font = cv2.FONT_HERSHEY_DUPLEX 
                    ret, frame = self.cap.read()
                    cv2.putText(frame, str(timer), (220, 250), font, 6, (255, 0, 0), 4, cv2.LINE_AA)
                    cv2.imshow('frame', frame)
                    current_time = time.time()
                    if current_time - start_time >= 1:
                        timer-=1 #increment timer down by 1 second
                        
                else:    #if timer is equal to zero show Start! on the screen
                    ret, frame = self.cap.read()
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, 'Start!', (200, 250), font, 5, (255, 145, 0), 4, cv2.LINE_AA)
        
                    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                    image_np = np.array(resized_frame)
                    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                    self.data[0] = normalized_image
                    #print(round((current_time-start_time)))
                    cv2.imshow('frame', frame)

                    self.get_computer_choice
                    self.get_user_choice
                    self.get_winner

                    if self.rounds_played == 3:
                        self.get_game_winner
                        self.cap.release()#Closes video file or capturing device/camera
                        print(f'You played 3 rounds, the game is finished.')
                        break

            elif cv2.waitKey(80) & 0xFF == ord('q'):
                print(f'You left game before 3 rounds')
                break
         
            #reinitialise timer back to 3s - to prepare for another round
            else:
                timer = 3


if __name__ == '__main__':

    game = rock_paper_scissors()
    game.play_game()


