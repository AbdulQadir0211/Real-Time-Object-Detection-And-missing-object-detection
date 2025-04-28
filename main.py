# main.py
import cv2
from modules.detector import ObjectDetector
from modules.tracker import ObjectTracker
from modules.scene_manager import SceneManager

def main():
    detector = ObjectDetector()
    tracker = ObjectTracker()
    scene = SceneManager()

    cap = cv2.VideoCapture(0)  # webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        tracked = tracker.update(detections)
        new_ids, missing_ids = scene.analyze(tracked)

        for obj in tracked:
            x1, y1, x2, y2 = map(int, obj['bbox'])
            label = f"{obj['class']} ID:{obj['track_id']}"
            color = (0, 255, 0) if obj['track_id'] not in missing_ids else (0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        for nid in new_ids:
            cv2.putText(frame, f"New Object ID: {nid}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        for mid in missing_ids:
            cv2.putText(frame, f"Missing Object ID: {mid}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Real-Time Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
