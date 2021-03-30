import streamlit as st
import pandas as pd
import numpy as np
import time
from record import video_cap



st.title("Vitals-detection")
#st.sidebar.selectbox("Selections", options['Heart Rate'])
st.write(
    '''
    This application is aimed at measuring vital signs using signal processing and techniques such as photoplestimography and deep learning.

    _____________________________________________

    ''')


def record():
    if st.button('Record'):
        video_cap(),







## SIDE BAR
st.sidebar.write(
    '''
    ## Menu
    _______________________________________________

    '''
)


## MENU CONSTRUCTION
menu = ["Home","Detect vitals","Upload Files", "Demo File","FAQ"]
choice = st.sidebar.selectbox("",menu)
if choice =="Upload Files":
    st.subheader("Upload Video")
    video_file = st.file_uploader("Upload Video")

elif choice =="Demo File":
    st.subheader("Demo File")
    video_file = open('./data/data_test.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    '''
    * La función video solo admite mp4
    * La función admite np.arrays hasta urls.
    * st.video("https://www.youtube.com/watch?v=9TPY2Jyyplk&t=3095s")

    '''
elif choice == "Detect vitals":
    st.subheader("Select the vital signs you want to measure")
    st.write("_____________________________________________")
    pr = st.checkbox("Pulse Rate")
    rr= st.checkbox("Respiration rate")
    bd = st.checkbox("Body temperature")
    if pr:
        st.write("To start the process of measuring HR just click the button below and wait for the magic")
        record()

    if rr or bd:
        st.write("This feature its not avaible yet")

elif choice == "FAQ":
    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some long explanations about the algorithm pychv")



