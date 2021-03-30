import streamlit as st
import pandas as pd
import numpy as np
import time
from record import video_cap



st.title("Vitals-detection")
#st.sidebar.selectbox("Selections", options['Heart Rate'])



def record():
    if st.button('Record'):
        video_cap(),

    if st.button('Stop'):
        pass




## SIDE BAR
st.sidebar.write(
    '''
    ## Menu
    Here must be and explanation about the menu bar

    '''
)




## MENU CONSTRUCTION
menu = ["Detect symptoms","Upload Files", "Demo File","FAQ"]
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
elif choice == "Detect symptoms":
    record()



elif choice == "FAQ":
    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some long explanations about the algorithm pychv")



