import cv2
import os

class DataCollection():

    def __repr__(self): 
        return 'сбор данных'
    
    def oper(self, img):
        path = 'images'
        num = len(os.listdir(path))
        cv2.imwrite(os.path.join(path , f'trash{num}.jpg'), img)
        return {"annotated_frame":img}