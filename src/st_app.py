import streamlit as st
import pandas as pd
import numpy as np
import time






##options = pd.DataFrame({'Heart Rate':["pPPG", "BOS"],'OKR':["LastnameUser"]})


st.title("Vitals-detection")
#st.sidebar.selectbox("Selections", options['Heart Rate'])



# Function construction
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Analize')
if pressed:
    right_column.write(" Render the Video Capture feature")
    st.sidebar.write(
        '''
        This runs  pyVHR alogorithm

        ''',
        # Poner los indices del dataframe como opciones  de signos
        pd.DataFrame({'Patient Name':["User"], 'Vitals':["10 bpm"]})

    )










expander = st.beta_expander("FAQ")
expander.write("Here you could put in some long explanations about the algorithm pychv")
