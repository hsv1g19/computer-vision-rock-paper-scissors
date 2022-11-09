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
start_time=time.time()
while True:
    timer=3
    start_time=time.time()
    while timer > 0:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        cv2.imshow('frame', frame)
        current_time=time.time()
        if current_time-start_time > 1:
            start_time = current_time
            timer-=1
    else:
         prediction = model.predict(data)

   # timer_countdown=3 #3seconds 
  
    #if round((current_time-start_time)) == 10:
     #   prediction = model.predict(data)        
      #  break
        
    #second while loop-outside define timer get the current time and store in variable
    # define another variable for for current time then use an if statent if difference between start and end is >1
        
        # Press q to close the window
        #print(prediction)
       #
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:

        timer = int(3)
    
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


#print("total time taken this loop: ", end_time - start_time)

def get_prediction(prediction):
    """_summary_

    Parameters
    ----------
    prediction : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    #out_dict={'rock':0, 'paper':1, 'scissors':2, 'nothing':3}
    #filtered_list=[{out_dict[key] for key in output if key in out_dict }]
    max_val_index= np.argmax(prediction) #idex of the higest probability
    if max_val_index ==0:
        choice='rock'
    if max_val_index ==1:
        choice='paper'
    if max_val_index == 2:
        choice='scissors'
    if max_val_index == 3:
        choice = 'nothing'
    return print(f"You chose {choice}")


get_prediction(prediction)