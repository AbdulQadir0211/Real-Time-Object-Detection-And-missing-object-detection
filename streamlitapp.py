# streamlit_app.py
import streamlit as st
import cv2
import tempfile
import time
from modules.detector import ObjectDetector
from modules.tracker import ObjectTracker
from modules.scene_manager import SceneManager

st.title("Real-Time Object Detection (Missing/New Object Tracking)")

run_detection = st.button("Start Detection")

if run_detection:
    stframe = st.empty()
    detector = ObjectDetector()
    tracker = ObjectTracker()
    scene_manager = SceneManager()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
    else:
        output_fps = []
        while True:
            start_time = time.time()
            ret, frame = cap.read()
            if not ret:
                break

            detections = detector.detect(frame)
            tracked_objects = tracker.update(detections)
            missing_ids, new_ids = scene_manager.update(tracked_objects)

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

            fps = 1 / (time.time() - start_time)
            output_fps.append(fps)
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame, channels="RGB", use_column_width=True)

        cap.release()
        st.success(f"Average FPS: {sum(output_fps)/len(output_fps):.2f}")
