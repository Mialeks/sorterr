import numpy as np
import cv2
import serial
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
port = serial.Serial('/dev/ttyACM0')
baudrate=9600
cap.set(3,320)
cap.set(4,240)

cap1 = cv2.VideoCapture(2)
#cap.set(cv2.CAP_PROP_FPS, 60)
cap1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
cap1.set(3,320)
cap1.set(4,240)
while(1):
    ret, frame = cap.read()
    ret, frame1 = cap1.read()
    if not ret:
        break
     # define range of blue color in HSV
    lower_blue = np.array([000,94,000])
    upper_blue = np.array([82,253,255])

    lower_blue1 = np.array([000,59,000])
    upper_blue1 = np.array([28,255,255])

    frames = frame[100:170, 140:200]
    frames1 = frame1[70:140, 130:200]

    hsv = cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)
    hsv1 = cv2.cvtColor(frames1, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask1 = cv2.inRange(hsv1, lower_blue1, upper_blue1)
    
    contours, hierarchy = cv2.findContours(mask,  
         cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    contours1, hierarchy1 = cv2.findContours(mask1,  
         cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    #cv2.imshow('Canny Edges After Contouring', edged) 
    #cv2.waitKey(0) 
    wyjscie = 0
    abc = len(contours)
    abc1 = len(contours1)
    if abc > 0 or abc1 > 0:
      wyjscie = 1
         
    else:
      wyjscie = 0
        
    print(wyjscie)
    print("Number of Contours found = " + str(len(contours))) 
    wyjscie1 = str(wyjscie)
    port.write(wyjscie1 + '\n')
# Draw all contours 
# -1 signifies drawing all contours 
   # cv2.drawContours(mask, contours, -1, (0, 255, 0), 3) 
    
    cv2.imshow('Contours', mask) 

    if ret == True:
        


        cv2.imshow('framee', mask1)
        cv2.imshow('framee1', frame)
        cv2.imshow('framee2', frame1)   
    else:
        cap.release()
        break
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
