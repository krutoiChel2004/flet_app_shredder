import cv2
import os

from utils.json_utils import(json_read)

class DataCollection():

    def __repr__(self): 
        return 'сбор данных'
    
    def oper(self, img):
        path = json_read()["frame_save_directory"]
        num = len(os.listdir(path))
        cv2.imwrite(os.path.join(path , f'img{num}.jpg'), img)
        return img