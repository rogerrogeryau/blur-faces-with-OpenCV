import cv2
import time

cap = cv2.VideoCapture('./carrie_lam_2.mp4')


face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
def detect_face(face_img):
    
    #display_img(img)
    
    #face_img = img.copy()
  
    face_rects = face_cascade.detectMultiScale(face_img) 
#     for fr in face_rects:
#         print(fr)
        
    for (x,y,w,h) in face_rects:
        face_img[y:y+h,x:x+w] = cv2.medianBlur(face_img[y:y+h,x:x+w],35)
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 2) 
        #display_img(face_img[y:y+h,x:x+w])
    
        
        #display_img(cv2.medianBlur(face_img[y:y+h,x:x+w],15))
    
#     print(f'face_rects: {len(face_rects)}')
    
    
    
    return face_img







# FRAMES PER SECOND FOR VIDEO
fps = 50


if cap.isOpened()== False: 
    print("Error opening the video file. Please double check your file path for typos. Or move the movie file to the same location as this script")
    

# While the video is opened
while cap.isOpened():
    

    ret, frame = cap.read()

    if ret == True:
        

        time.sleep(1/fps*2)
        
        frame = detect_face(frame)
        
        cv2.imshow('frame',frame)
 
        # Press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            break
 
    # Or automatically break this whole loop if the video is over.
    else:
        break
        
cap.release()
# Closes all the frames
cv2.destroyAllWindows()