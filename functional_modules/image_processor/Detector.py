import threading

from functional_modules.image_processor.Model import Model_YOLO

from utils.database_utils import insert_TrashStatTable
from utils.messege_bot_utils import send_photo_TG



class Detector(Model_YOLO):       
    def __repr__(self): 
        return 'детекция'

    def oper(self, frame):
        result_ptred = super(Detector, self).oper(frame)

        annotated_frame = result_ptred["annotated_frame"]
        list_cls = result_ptred["list_cls"]
        
        if list_cls is not None:
            thr_writing_trash_class_database = threading.Thread(target=insert_TrashStatTable, args=(list_cls,), name="thr-writing_trash_class_database")
            thr_send_photo_TG = threading.Thread(target=send_photo_TG, args=(annotated_frame, list_cls,), name="thr-send_photo_TG")

            thr_writing_trash_class_database.start()
            thr_send_photo_TG.start()

        return annotated_frame