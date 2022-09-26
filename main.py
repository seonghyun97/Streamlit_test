import streamlit as st
from PIL import Image
import os
import sys
import glob
import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image
import numpy as np
treamlit = "cool"
theming = "fantastic"
both = "💥"
st.set_page_config(layout="wide")
st.title("# canAIry 열화상카메라⭐️")

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("## Before💥")
    uploaded_file = st.file_uploader("Choose a file")
    result = 0
    if uploaded_file:
        image = Image.open(uploaded_file)
        im2arr = np.array(image)  # im2arr.shape: height x width x channel
        arr2im = Image.fromarray(im2arr)
        arr2im.save('yolov5/runs/detect/origin/test.jpg')
        st.image(image)
        result = st.button("Convert")
    else:
        pass


with col2:
    st.markdown("## After💥")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    if result:
        terminal_command = "python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best2.pt --img 256 --conf 0.1 --source yolov5/runs/detect/origin/test.jpg"
        os.system(terminal_command)
        result_path = glob.glob("yolov5/runs/detect/exp/*")
        image = Image.open(result_path[0])
        st.image(image)
        os.system(
            "rm -rf yolov5/runs/detect/exp")
        os.system(
            "rm -rf yolov5/runs/detect/origin/test.jpg")
    else:
        pass
