# main_pipeline.py
import cv2
import time
from modules.detector import ObjectDetector
from modules.tracker import ObjectTracker
from modules.scene_manager import SceneManager

class ObjectDetectionPipeline:
    def __init__(self):
        self.detector = ObjectDetector()
        self.tracker = ObjectTracker()
        self.scene_manager = SceneManager()

    def run(self):
        cap = cv2.VideoCapture(0)  # Webcam
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        output_fps = []
        while True:
            start_time = time.time()
            ret, frame = cap.read()
            if not ret:
                break

            detections = self.detector.detect(frame)
            tracked_objects = self.tracker.update(detections)
            missing_ids, new_ids = self.scene_manager.update(tracked_objects)

            for obj in tracked_objects:
                x, y, w, h = obj['bbox']
                label = f"{obj['class']} {obj['id']}"
                color = (0, 255, 0)
                if obj['id'] in new_ids:
                    label += " (New)"
                    color = (255, 0, 0)
                elif obj['id'] in missing_ids:
                    label += " (Missing)"
                    color = (0, 0, 255)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Calculate FPS
            end_time = time.time()
            fps = 1 / (end_time - start_time)
            output_fps.append(fps)
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            cv2.imshow("Object Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        avg_fps = sum(output_fps) / len(output_fps)
        print(f"Average FPS: {avg_fps:.2f}")

if __name__ == '__main__':
    pipeline = ObjectDetectionPipeline()
    pipeline.run()