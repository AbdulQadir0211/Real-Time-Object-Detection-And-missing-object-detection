# streamlit_app.py
import streamlit as st
import cv2
from main_pipeline import run_detection_stream
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.set_page_config(page_title="Real-Time Object Monitor", layout="wide")
st.title("📦 Real-Time Object Detection and Monitoring")
st.markdown("Detects **new** and **missing** objects in live webcam stream using YOLOv8 + DeepSORT")

run = st.button("Start Webcam Detection")

if run:
    stframe = st.empty()
    for frame in run_detection_stream():
        # Convert BGR (OpenCV) to RGB (Streamlit)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB")
