##Calculations and evaluation of mouse gesture
import HandDetctionModule as hdm
import cv2

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    frame = hdm.detectHand(frame)
    #x,y,z = hdm.detectCase()
    #print("x : ",x,"y : ",y,"z : ",z)
    #hdm.detectCase(locs)
    cv2.imshow("hello",frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
