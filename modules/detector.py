# detector.py
from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self, model_name='yolov8n.pt'):
        self.model = YOLO(model_name)

    def detect(self, frame):
        results = self.model(frame)[0]
        detections = []
        for r in results.boxes:
            x1, y1, x2, y2 = map(int, r.xyxy[0])
            conf = float(r.conf)
            cls = int(r.cls)
            label = self.model.names[cls]
            detections.append({
                'bbox': [x1, y1, x2 - x1, y2 - y1],
                'confidence': conf,
                'class': label
            })
        return detections
