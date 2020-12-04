import numpy as np
import cv2
import serial
import time
from twilio.rest import Client
account_sid = 'AC46cd398efb88f0cd0fbd601977b5f5f0'
auth_token = '6258ed1c02ddbc1a9a0fb4799dff2d99'
client = Client(account_sid, auth_token)
check_sms = 0
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img, 1.2, 5)
    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if(check_sms >= 3):
           # message = client.messages.create(to="+923445034342", 
            #           from_="+12058465355", 
             #          body="Fire Alert !      Fire Alert !")
            #print(message.sid)
            check_sms = 0
        check_sms = check_sms + 1
        print ('Fire is detected..!')
        time.sleep(0.2)
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
