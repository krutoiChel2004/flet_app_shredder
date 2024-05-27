from ultralytics import YOLO

from utils.json_utils import json_read

class Model_YOLO():
    def __init__(self, conf:float = 0.7) -> None:
        path_nn_model = "flet_app_shredder\\nn_models\\"
        name_nn_model = json_read()["selected_nn_models"]
        model = YOLO(path_nn_model + name_nn_model)
        self.model = model.to("cuda")
        self.conf = conf

    def oper(self, img):
        model_pred = self.model(img, conf=self.conf, verbose=False, imgsz=480)

        if model_pred[0].boxes:
            annotated_frame = model_pred[0].plot()
            list_cls = model_pred[0].boxes.cls
        else:
            annotated_frame = img
            list_cls = None
        return {"annotated_frame": annotated_frame,
                "list_cls": list_cls}
