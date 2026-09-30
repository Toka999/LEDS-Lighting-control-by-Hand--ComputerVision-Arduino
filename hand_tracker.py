#.......packages needed.......
import mediapipe as mp     # for machine learning package
import cv2                 # for camera view package
import arduinocontrol as ac
import time

#..........................................................
time.sleep(2.0)

cap=cv2.VideoCapture(0)    # store video recording from computer's camera of value 0 in variable cap
mpHands=mp.solutions.hands #store solutions for hands of media pipe in mpHands
hands=mpHands.Hands()      
mpDraw=mp.solutions.drawing_utils #store hand drawings in mp hands
tipIds=[4,8,12,16,20]
while True:
 # assign two variables to store readings of cap in them
    success,img = cap.read() 

# to flip the camera iamage horizontally 
    img=cv2.flip(img,1) 

# variable that changes image stored in img from BGR to RGB to be resolved
    imgRGB= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
# the image stored in imgRGB is going to be processed and stored in results 
    results= hands.process(imgRGB)


    #tipid=[4,8,16,20,12] 
    lmList=[] 
    fingers=[]
#see if the hand land marks are detected or not
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
          for id,lm in enumerate(handLms.landmark):
              h, w, c =img.shape                   #store height, width, center, of video window
              cx ,cy =int(lm.x * w), int(lm.y * h) #center coordiantes
              lmList.append([id,cx,cy])            # add id ,cx,cy into the empty list
              mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  # to plot and draw hand connections on hand image on screen
              #print(lmList)
              #print(results.multi_hand_landmarks) 
              for id in enumerate(handLms.landmark):
                 cv2.circle(img,(cx,cy),10,(255,100,255),cv2.FILLED) # to identify size and color of the plot
                 if len (lmList)==21:
                    if lmList[8][2] < lmList[6][2] :
                       fingers.pop
                       print("one")
                       fingers.append(1)
                       #cv2.rectangle(img,(20,20),(20,20),(0,0,0),cv2.FILLED)       
                       cv2.rectangle(img,(20,300),(270,425),(0,255,0))
                       cv2.putText(img,"1 LED",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                       ac.led(fingers)
                       
                    #if lmList[8][2] < lmList[6][2] and lmList[12][2]< lmList[10][2] :
                       print("two")
                       cv2.rectangle(img,(20,300),(270,425),(0,255,0))
                       cv2.putText(img,"2 LED",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                       ac.led(fingers)
                       
                    elif lmList[8][2]< lmList[6][2] and lmList[12][2]<lmList[10][2]and lmList[16][2]< lmList[14][2] or lmList[20][2]<lmList[18][2]and  lmList[16][2]< lmList[14][2]and lmList[12][2]< lmList[10][2]:
                       fingers.pop
                       print("three")
                       fingers.append(3)
                       cv2.rectangle(img,(20,300),(270,425),(0,255,0))
                       cv2.putText(img,"3 LED",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                       ac.led(fingers)
                    #if lmList[8][2]< lmList[6][2] and lmList[12][2]< lmList[10][2] and lmList[16][2]<lmList[14][2]and lmList[20][2]<lmList[18][2]and lmList[3][2]>lmList[9][2] :
                       print("four")
                       
                       cv2.rectangle(img,(20,300),(270,425),(0,255,0))
                       cv2.putText(img,"4 LED",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                    #if lmList[8][2]< lmList[6][2] and lmList[12][2]< lmList[10][2] and lmList[16][2]<lmList[14][2]and lmList[20][2]<lmList[18][2]and lmList[4][2]<lmList[2][2] :
                      # print("five")
                       #cv2.rectangle(img,(20,300),(270,425),(0,255,0))
                       #cv2.putText(img,"5 LED",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                    elif  lmList[8][2]>lmList[5][2] and lmList[12][2]>lmList[9][2]and lmList[16][2]>lmList[13][2] and lmList[20][2]>lmList[17][2]:
                       fingers.pop
                       print("zero")
                       fingers.append(0)
                       cv2.rectangle(img,(20,300),(270,425),(0,255,0))
                       cv2.putText(img,"0 LED ",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                       ac.led(fingers)
        cv2.imshow("hand tracker",img)
#close camera window if "esc" is pressed
        if cv2.waitKey(5)& 0xff==27:
         break
        
''' if len(lmList)!=0:
       if lmList[tipid[0]][1]>lmList[tipid[0]-1][1]:
          fingers.append(1)
    else:fingers.append(0)
    for id in range(1,5):
       if lmList[tipid[id]][2]<lmList[tipid[id]-2][2]:
         fingers.append(1)
       else:
          fingers.append(0)
    total=fingers.count(1)
    if total==0:
       cv2.rectangle(img,(20,300),(270,425),(0,0,0),cv2.FILLED)       
       cv2.putText(img,"0",(45,375),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0),5)'''
    
# open the camera view with a title "hand tracker" and the data stored from camera in img

'''mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands
tipIds=[4,8,12,16,20]
video=cv2.VideoCapture(0)
with mp_hand.Hands(min_detection_confidence=0.2,min_tracking_confidence=0.2,max_num_hands=2) as hands:
    while True:
        ret,image=video.read()
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id,lm in enumerate(myHands.landmark):
                    h,c,w=image.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_draw.draw_landmarks(image,hand_landmark,mp_hand.HAND_CONNECTIONS)
                fingers=[]
                if len(lmList)!=0:
                  if lmList[tipIds[0]][2]> lmList[tipIds[0]-1][2]:
                        fingers.append(1)
                  else:
                        fingers.append(0)
                  for id in range(1,5):
                     if lmList[tipIds[0]][2]<lmList[tipIds[id]-1][2]:
                         fingers.append(1)
                     else:
                         fingers.append(0)
                  total=fingers.count(1)
                  #ac.led(total)
                  if total==0:
                   cv2.rectangle(image,(20,300),(270,425),(0,255,0))
                   cv2.putText(image,"0",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                  elif total==1:
                   cv2.rectangle(image,(20,300),(270,425),(0,255,0))
                   cv2.putText(image,"1",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                  elif total==2:
                   cv2.rectangle(image,(20,300),(270,425),(0,255,0))
                   cv2.putText(image,"2",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                  elif total==3:
                   cv2.rectangle(image,(20,300),(270,425),(0,255,0))
                   cv2.putText(image,"3",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                  elif total==4:
                   cv2.rectangle(image,(20,300),(270,425),(0,255,0))
                   cv2.putText(image,"4",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
                  elif total==5:
                   cv2.rectangle(image,(20,300),(270,425),(0,255,0))
                   cv2.putText(image,"5",(45,375),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
        cv2.imshow("camera view",image)
        k=cv2.waitKey(1)
        if k==ord('q') or k==ord('Q'):
            break
video.release()
cv2.destroyAllWindows()'''