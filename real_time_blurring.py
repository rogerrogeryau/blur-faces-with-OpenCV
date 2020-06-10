import cv2
import numpy as np
# import matplotlib.pyplot as plt

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



#     face_img = img.copy()
#     roi = img.copy()
# #     face_detect = face_cascade.detectMultiScale(face_img,scaleFactor=1.3, minNeighbors=3) 
#     face_detect = face_cascade.detectMultiScale(face_img) 
# #     for (x,y,w,h) in face_detect: 

# #     print("--------")

# #     print(f'face_detect: {len(face_detect)}')

#     for (x,y,w,h) in face_detect: 
# #         print(x,y,w,h)
        
#         roi = roi[y:y+h,x:x+w]
        
#         print(roi.shape)
        
# #         display_img(roi)
        
# #         blurred_roi = cv2.medianBlur(roi,75)
# #         face_img[y:y+h,x:x+w] = blurred_roi
        
# #     print(blurred_roi.shape)
    
    
#     return face_img
        

if __name__ == "__main__":
    cap = cv2.VideoCapture(0) 
    while True: 
    
        ret, frame = cap.read(0)
        frame = detect_face(frame)
        cv2.imshow('Video Face Detection', frame) 
        c = cv2.waitKey(1) 
        if c == 27: 
            break 
    cap.release() 
    cv2.destroyAllWindows()
