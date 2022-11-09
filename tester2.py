import random
import cv2
import time
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


#output = []
#end_time = time.time()+2#  time after epoch time January 1st, 1970 , The time. time() function returns the number of seconds since the epoch
#The time. time() function returns the number of seconds since the epoch
#while end_time>time.time()


#print("total time taken this loop: ", end_time - start_time)
rounds_played=0
computer_wins=0
user_wins=0

def get_prediction():
    start_time=time.time()
    while True:
 
        current_time=time.time()
    # timer_countdown=3 #3seconds 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        print(round((current_time-start_time)))
        cv2.imshow('frame', frame)
        if round((current_time-start_time)) == 3:
            prediction = model.predict(data)   
        if rounds_played == 3:
            get_game_outcome()
            stop_video()
    
            break
        
        #second while loop-outside define timer get the current time and store in variable
        # define another variable for for current time then use an if statent if difference between start and end is >1
        
            # Press q to close the window
            #print(prediction)
       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    #out_dict={'rock':0, 'paper':1, 'scissors':2, 'nothing':3}
    #filtered_list=[{out_dict[key] for key in output if key in out_dict }]
    max_val_index= np.argmax(prediction[0]) #idex of the higest probability
    return options[max_val_index]

def get_user_choice():
    
    return print(f"you chose {get_prediction()}") #prints what the use has selected







options=["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(options).lower()




def  get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        winner= print(f"Both players selected {user_choice}. It's a tie!")
        rounds_played+=1
    elif user_choice == "rock":
        if computer_choice == "scissors":
            winner= print("Rock smashes scissors! You win!")
            rounds_played+=1
            user_wins+=1
        else:
            winner= print("Paper covers rock! You lose computer won.")
            rounds_played+=1
            computer_wins+=1
    elif user_choice == "paper":
        if computer_choice == "rock":
            winner= print("Paper covers rock! You win!")
            rounds_played+=1
            user_wins+=1
        else:
            print("Scissors cuts paper! You lose computer won.")
            rounds_played+=1
            computer_wins+=1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            winner=print("Scissors cuts paper! You win!")
            rounds_played+=1
            user_wins+=1
        else:
            winner=print("Rock smashes scissors! You lose computer won.")
            rounds_played+=1
            computer_wins+=1



def play():
    
    human_choice=get_prediction()
    computer_choice=get_computer_choice()
    return get_winner(computer_choice, human_choice )
    

play()


