import streamlit as st
import pandas as pd
import numpy as np
import time
import record as r
# import vh Trae sin problemas la librería





## CONFIG STREAMLIT

st.set_page_config(
    page_title ="Vital-detection",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)





st.title("Vitals-detection")
#st.sidebar.selectbox("Selections", options['Heart Rate'])
st.write(
    '''
    This application is aimed at measuring vital signs using signal processing and techniques such as photoplestimography and deep learning. To start the magic, you can look up the context in the menu on the left and we'll walk you through it.

    _____________________________________________

    ''')


def record():
    if st.button('Record'):
        r.video_cap()
        status_v= st.progress(0)
        for percent in range(10):
            time.sleep(0.2)
        st.success('You can check your vitals at "Results"!')
        # vh_data = vh
        




## SIDE BAR
st.sidebar.write(
    '''
    ## Menu
    _______________________________________________

    '''
)


#sample
hr_array = [65.0390625 , 64.16015625 ,65.91796875 ,65.91796875, 65.0390625 , 65.91796875,
        67.67578125 ,66.796875  , 64.16015625, 61.5234375 , 64.16015625, 67.67578125,
        65.91796875 ,63.28125 ,  60.64453125 ,61.5234375,  64.16015625, 65.91796875,
        64.16015625 ,61.5234375 , 59.765625  ]

hr_result = np.mean(hr_array)


## MENU CONSTRUCTION
menu = ["Home","Detect vitals","Upload Files","Results", "Demo File","FAQ"]
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
        st.write("To start the heart rate measurement process, simply click the button below and wait 10 seconds to record the magic")
        record()

    if rr or bd:
        st.write("This feature its not avaible yet")

elif choice == "FAQ":
    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some long explanations about the algorithm pychv")


elif choice == "Results":
    

# CONTAINER IMAGE
    image_displayer, data_displayer = st.beta_columns(2)

    with image_displayer:
        st.image('./data/image.png')


    with data_displayer:
        data_displayer.write("HR-bpm")
        data_displayer.write(hr_result)


