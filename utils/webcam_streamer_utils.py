import cv2
import base64

from functional_modules.image_processor.Detector import Detector
from functional_modules.image_processor.DataCollection import DataCollection

my_detector = Detector()
my_data_collector = DataCollection()

operating_mode = {"детекция": my_detector,
                  "сбор данных": my_data_collector}

def process_frame(operating_mode_value, frame):
    # Обрабатывает кадр и возвращает изображение в формате Base64
    pred = operating_mode[operating_mode_value].oper(frame)
    
    _, jpg_img = cv2.imencode('.jpg', pred)
    b64_string = base64.b64encode(jpg_img).decode('utf-8')

    return {"img_b64_string":b64_string}