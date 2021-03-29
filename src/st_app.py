import streamlit as st
import pandas as pd
import numpy as np
import time
from record import video_cap




##options = pd.DataFrame({'Heart Rate':["pPPG", "BOS"],'OKR':["LastnameUser"]})


st.title("Vitals-detection")
#st.sidebar.selectbox("Selections", options['Heart Rate'])



# Function construction
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Record')
if pressed:
    right_column.write(" Render the Video Capture feature")
    st.sidebar.write(
        '''
        This runs  pyVHR alogorithm

        ''',
        video_cap(),
        
        # Poner los indices del dataframe como opciones  de signos
        pd.DataFrame({'Patient Name':["User"], 'Vitals':["10 bpm"]})

    )

analized = left_column.button('Analize')
stop = left_column.button('Stop')











expander = st.beta_expander("FAQ")
expander.write("Here you could put in some long explanations about the algorithm pychv")
