import time
import asyncio

import cv2
import numpy as np
import pandas as pd
import streamlit as st

import module_vhr as vhr
import record as r

## CONFIG STREAMLIT



st.set_page_config(
    page_title ="Vital-detection",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)




def main():

    ## TITTLE
    st.title("Vital-detection")
    st.write(
        '''
        This application is aimed at measuring vital signs using signal processing and techniques such as photoplestimography 
        and deep learning. To start the magic, you can look up the context in the menu on the left and we'll walk you through it.

        _____________________________________________

        ''')


    ## SIDE BAR
    st.sidebar.write(
        '''
        ## Menu
        _______________________________________________

        '''
    )


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

    elif choice == "Detect vitals":
        st.subheader("Select the vital signs you want to measure")
        st.write("_____________________________________________")
        pr = st.checkbox("Pulse Rate")
        #rr= st.checkbox("Respiration rate")
        #bd = st.checkbox("Body temperature")

        if pr:
            st.write("To start the heart rate measurement process, simply click the button below and wait 10 seconds to record the magic")
            record()
            asyncio.run(analize())

        #if rr or bd:
            #st.write("This feature its not avaible yet")

    elif choice == "FAQ":
        expander = st.beta_expander("FAQ")
        expander.write("Here you could put in some long explanations about the algorithm pychv")

    # CONTAINER IMAGE
    elif choice == "Results":
        image_displayer, data_displayer = st.beta_columns(2)
        with image_displayer:
            image = cv2.imread('./data/image.png')
            st.image(image, caption='Results')


        with data_displayer:
            data_displayer.write("HR-bpm")
            data_displayer.write( results)


async def analize():
    await asyncio.sleep(13)
    results = vhr.chrom()
    return results



def record():
    if st.button('Record'):
        r.video_cap()
        status_v = st.progress(0)
        for percent in range(10):
            time.sleep(0.2)
        st.success('You can check your vitals at "Results"!')

        

if __name__ =="__main__":
    main()