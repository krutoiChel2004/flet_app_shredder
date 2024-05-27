from ultralytics import YOLO

def training_func(model:str, 
                  epochs:int, 
                  imgsz:int, 
                  batch:int, 
                  device:str):
    model_dict = {
        "YOLOv8n":"yolov8n.pt",
        "YOLOv8s":"yolov8s.pt",
        "YOLOv8m":"yolov8m.pt",
        "YOLOv8l":"yolov8l.pt",
        "YOLOv8x":"yolov8x.pt",
    }

    device_dict = {
        "GPU":0,
        "CPU":"cpu"
    }

    model:YOLO = YOLO(model_dict[model])

    result = model.train(data="coco8.yaml", 
                epochs=epochs, 
                imgsz=imgsz, 
                device=device_dict[device],
                batch=batch,)

