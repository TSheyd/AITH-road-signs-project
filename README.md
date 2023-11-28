# AITH-road-signs-project
AI Talent Hub Deep Learning Practice Course - road signs detection

---
 
## Table of contents

- [Dataset](#dataset)
- [Model architecture](#model-architecture)
- [MVP](#mvp)

## Dataset
We used [russian-traffic-signs-recognition Image Dataset](https://universe.roboflow.com/mguogareva/russian-traffic-signs-recognition/dataset/3) for final model. See more in [second branch](https://github.com/TSheyd/AITH-road-signs-project/tree/grishaechka)


## Model Architecture
For model, YOLOv8 nano was used. Check the [second branch](https://github.com/TSheyd/AITH-road-signs-project/tree/grishaechka) for more info on training and experiments

## MVP
Although the app is supposed to run on mobile, within this course we do a simpler approach with a demo web app. There you can upload a video, get it processed and see the results. 
The web app provides the processed video, as well as the list of detected items

### Deployment
1. Make sure you have Python 3.8 or newer installed. We used 3.11.
2. Install required packages with `pip install requirements.txt`
3. Run Streamlit app: `streamlit run path_to_project\AITH-road-signs-project\streamlit_app.py`
4. If browser window did not open automatically, go to `http://localhost:8501/`

