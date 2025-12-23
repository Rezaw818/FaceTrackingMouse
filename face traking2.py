import cv2
import pyautogui as robot

face_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_model = cv2.CascadeClassifier("haarcascade_eye.xml")

loop = True
cam = cv2.VideoCapture(0)
while loop:
    
    _, img = cam.read()
    
    img = cv2.flip(img, 1)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_model.detectMultiScale(img)
    eye = []
    
    out = img.copy()
    if len(face) > 0:
          x = face[0][0]
          y= face[0][1]
          x2 = face[0][0] + face[0][2]
          y2 = face[0][1] + face[0][3]
          if(x<200 or y<140 or x2 >450 or y2 > 400):
                 cv2.rectangle(out, (x,y), (x2, y2), (255, 255, 255), 3)
          else:
             cv2.rectangle(out, (x,y), (x2, y2), (250, 0, 0), 3)          
          cv2.rectangle(out, (200,140), (450, 400), (250, 0, 0), 3)
          eye = eye_model.detectMultiScale(out[y:y2 , x:x2])
        
    
        
       
    eyeCount = 0   
    if len(eye) > 0:      
      for (xe,ye,we,he) in eye:
            eyeCount = eyeCount+1
            cv2.rectangle(out, (xe+x,ye+y) , (xe+we+x ,ye+he+y), (0,250,0), 3) 
            if eyeCount == 2:
                  break
              
          
               
            
    cv2.imshow("mycam", out)  
    if cv2.waitKey(1) == ord("q"):
      loop = False 
      cv2.destroyAllWindows()
      cam.release()
      break
    
    mouse_x = robot.position().x  
    mouse_y = robot.position().y
    if y < 140 and x2 > 450 :
      mouse_x = mouse_x + abs(x2 - 450)
      mouse_y = mouse_y - abs(y - 140)
      robot.moveTo(mouse_x, mouse_y, duration=0.5)  
    elif y2 > 400 and x2 > 450 :
      mouse_x = mouse_x + abs(x2 - 450)
      mouse_y = mouse_y + abs(y2 - 400)
      robot.moveTo(mouse_x, mouse_y, duration=0.5)  
    elif y2 > 400 and x < 200 :
      mouse_x = mouse_x - abs(x - 200)
      mouse_y = mouse_y + abs(y2 - 400)
      robot.moveTo(mouse_x, mouse_y, duration=0.5)  
    elif y < 140 and x < 200 :
      mouse_x = mouse_x - abs(x - 200)
      mouse_y = mouse_y - abs(y - 140)
      robot.moveTo(mouse_x, mouse_y, duration=0.5)  
    elif x<200 :
      mouse_x =  mouse_x - abs(x - 200)
      robot.moveTo(mouse_x,mouse_y,0.1)
      
    elif x2>450:
      mouse_x =  mouse_x + abs(x2 - 450)
      robot.moveTo(mouse_x,mouse_y,0.1)
      
    elif y < 140:
      mouse_y = mouse_y - abs(y - 140)
      robot.moveTo(mouse_x, mouse_y, 0.1)
      
    elif y2 > 400:
      mouse_y = mouse_y + abs(y2 - 400)
      robot.moveTo(mouse_x, mouse_y, 0.1)
      