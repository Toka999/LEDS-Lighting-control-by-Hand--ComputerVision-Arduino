'''
1]install python 3.7 to be applicable with the used libraries

2] please before running the code type the following instructions in the terminal to avoid any errors:
pip3.7 install cv.py.............> library for camera vision
pip3.7 install mediapipe.........>library for machine learning 
pip3.7 install cvzone............>
pip3.7 install numpy.............>library to deal with lists faster
pip3.7 install pyfirmata.........>library that connect python with arduino (operates only with python 3.7 not further versions)
  
'''




#........import needed libraries and file..................................
import cv2                                  #import camera vision 
import controller as cnt                    #import pre-programmed file for python-arduino sync
from cvzone.HandTrackingModule import HandDetector  #import camera vision zone for hand tracking
 #.........................................................................
detector=HandDetector(detectionCon=0.8,maxHands=1)    
video=cv2.VideoCapture(0)           #store data from camera in a variable
                            
#start a non-stoping loop for continues detection
while True:
    ret,frame=video.read()           #assign two vars. to store the parameters of read function
    frame=cv2.flip(frame,1)          #flip camera image and store it in a var.
    hands,img=detector.findHands(frame)               
    if hands:
        lmList=hands[0]                               
        fingerUp=detector.fingersUp(lmList)          



        print(fingerUp)
        cnt.led(fingerUp)                      # call the controller file
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)    
        elif fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA) 

    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord("k"):
        break

video.release()
cv2.destroyAllWindows()
