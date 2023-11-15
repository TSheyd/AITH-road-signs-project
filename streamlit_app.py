import streamlit as st
import pandas as pd
from pathlib import Path
import tempfile
import os
from ultralytics import YOLO
import moviepy.editor as moviepy

# Config
MODEL_PATH = "weights/sample.pt"
INFERENCE_CONFIG = {
    "conf": 0.01,
    "hide_conf": True,
    "max_det": 1,
    "classes": 0,
    "save": True,
    "project": "video_cache",
}

# Page config
st.set_page_config(layout="wide")
st.title("🚗 Road Signs Detection Demonstration App 🚗")

# Create a temporary directory within the project directory
temp_dir = Path("video_cache")
temp_dir.mkdir(parents=True, exist_ok=True)


# Initialize session state variables if they don't exist
if 'video_processed' not in st.session_state:
    st.session_state['video_processed'] = False

if 'locations' not in st.session_state:
    st.session_state['locations'] = None

if 'model' not in st.session_state:
    st.session_state['model'] = None


# Upload file section
uploaded_file = st.file_uploader("Upload a video...", type=["mp4", "mov", "avi", "asf", "m4v"])


# Load the model
if not st.session_state['model']:
    with st.spinner('Model preparation...'):
        # model weights for inference
        model = YOLO(MODEL_PATH)
        st.session_state['model'] = model


# Upload the file and run inference
if uploaded_file is not None and not st.session_state['video_processed']:
    with st.spinner('Extracting...'):

        # Upload file
        tfile = tempfile.NamedTemporaryFile(delete=False, dir=temp_dir, suffix='.mp4')
        tfile.write(uploaded_file.read())
        video_path = tfile.name
        tfile.close()

        # Run inference
        proc_filename = f"{os.path.split(video_path)[-1][:-4]}_processed"
        results = st.session_state['model'].predict(source=video_path, name=proc_filename, **INFERENCE_CONFIG)
        clear_filename = os.path.split(video_path)[-1]

        output_path = f"video_cache\\{proc_filename}\\{clear_filename[:-4]}.avi"

        # Convert to mp4 format so streamlit will show the vid
        clip = moviepy.VideoFileClip(output_path)
        clip.write_videofile(output_path.replace('avi', 'mp4'))
        os.remove(output_path)  # delete the .avi file

        # Set the output filepath to show (dataframe locations used)
        st.session_state["video_path"] = output_path.replace('avi', 'mp4')
        st.success('Sucessfully extracted!')

        # Save the session
        st.session_state['video_processed'] = True


# Layout for processed video
if st.session_state['video_processed']:
    output_vid, detections_col = st.columns([1, 1])

    with output_vid:
        st.header("Processed Video")
        st.video(st.session_state['video_path'])

    with detections_col:
        st.header("Detected Signs")  # todo
        st.table(pd.DataFrame(columns=['timestamp', 'sign', 'importance', 'confidence']))