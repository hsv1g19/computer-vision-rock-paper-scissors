import time
"""
from time import time

start_time=time()

count_down=11
while True:
    
    current_time=time()
    tim= round(current_time-start_time)
    for i in range(tim):
        if i>0:
            count_down-=1
    if count_down ==0 and tim==10:
        print('fuck you')
        break


start_time=time()
while True:
  
    prev = time.time()

                # if timer > 0 -timer is displayed on screen 
    
    while timer > 0:
        print('helooooooo')
        cur = time.time()
        print(cur-prev)           
        if cur - prev >= 1:
            #prev = cur
            timer = timer - 1
    
    else:
        print('done')
        break

"""

def get_prediction():
    start_time=time.time()
    timer=0
    while True:

        if round((start_time-current_time)) == 3:
            prediction = model.predict(data)   

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
