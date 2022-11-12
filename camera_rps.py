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


# def get_prediction():
#     start_time=time.time()
#     while True:
 
#         current_time=time.time()
#     # timer_countdown=3 #3seconds 
#         ret, frame = cap.read()
#         resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
#         image_np = np.array(resized_frame)
#         normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
#         data[0] = normalized_image
#         print(round((current_time-start_time)))
#         cv2.imshow('frame', frame)
#         if round((current_time-start_time)) == 3:
#             prediction = model.predict(data)
#             print(prediction)
#             break   
        
#         #second while loop-outside define timer get the current time and store in variable
#         # define another variable for for current time then use an if statent if difference between start and end is >1
        
#             # Press q to close the window
#             #print(prediction)
       
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # After the loop release the cap object
#     cap.release()
#     # Destroy all the windows
#     cv2.destroyAllWindows()
#     max_val_index= np.argmax(prediction) #idex of the higest probability
#     if max_val_index ==0:
#         choice='rock'
#     if max_val_index ==1:
#         choice='paper'
#     if max_val_index == 2:
#         choice='scissors'
#     if max_val_index == 3:
#         choice = 'nothing'
#     return print(f"You chose {choice}")



# get_prediction()



    
options = ['rock', "paper", "scissors", "nothing"]
while True:
    timer = 3
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    start_time=time.time()
    while timer > 0:
        font = cv2.FONT_HERSHEY_DUPLEX 
        ret, frame = cap.read()
        cv2.putText(frame, str(timer), (250, 250), font, 6, (255, 0, 0), 4, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(5)
        current_time = time.time()
        if current_time - start_time >= 1:
            start_time = current_time 
            timer-=1 #increment timer down by 1 second
                        
    else:  
                         #if timer is equal to zero show Start! on the screen
        
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image                #print(round((current_time-start_time)))
        cv2.imshow('frame', frame)
        prediction = model.predict(data)

        
    if cv2.waitKey(80) & 0xFF == ord('q'):
        print(f'You left game before 3 rounds')
        break
         
            #reinitialise timer back to 3s - to prepare for another round
    else:
        timer = 3

def get_prediction():
    max_val_index = np.argmax(prediction)
    if max_val_index == 3:
        user_choice = 'None'
    else:
        user_choice = options[max_val_index]
        print(f'You chose {user_choice}')

print(get_prediction())
    