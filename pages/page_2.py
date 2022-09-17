# Contents of ~/my_app/pages/page_2.py
import streamlit as st
from PIL import Image
import os, sys
import glob
import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image
import numpy as np

st.markdown("# Class 2")

col1, col2, col3 = st.columns([3,1,3])
with col1:
    st.markdown("## Before")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file:
        image = Image.open(uploaded_file)
        im2arr = np.array(image) # im2arr.shape: height x width x channel
        arr2im = Image.fromarray(im2arr)
        arr2im.save('C:\\Users\\ddiam\\Streamlit\\yolov5\\runs\\detect\\origin\\test.jpg')
        st.image(image, caption='Sunrise by the mountains')
    else:
        pass
    


with col2:
    result = st.button("Convert")

with col3:
    st.markdown("## After")
    if result:
        terminal_command = "python C:\\Users\\ddiam\\Streamlit\\yolov5\\detect.py --weights C:\\Users\\ddiam\\Streamlit\\yolov5\\runs\\train\\exp\\weights\\best.pt --img 256 --conf 0.1 --source C:\\Users\\ddiam\\Streamlit\\yolov5\\runs\\detect\\origin\\test.jpg"
        os.system(terminal_command)
        result_path = glob.glob("C:\\Users\\ddiam\\Streamlit\\yolov5\\runs\\detect\\exp\\*")
        image = Image.open(result_path[0])
        st.image(image)
        os.system("rmdir /s /q C:\\Users\\ddiam\\Streamlit\\yolov5\\runs\\detect\\exp")
        os.system("del /s C:\\Users\\ddiam\\Streamlit\\yolov5\\runs\\detect\\origin\\test.jpg")
    else:
        pass
    