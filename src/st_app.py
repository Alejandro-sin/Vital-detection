import streamlit as st
import pandas as pd
import numpy as np
import time






##options = pd.DataFrame({'Heart Rate':["pPPG", "BOS"],'OKR':["LastnameUser"]})


st.title("Vitals-detection")
#st.sidebar.selectbox("Selections", options['Heart Rate'])


if st.checkbox('Hearth Rate'):
    st.sidebar.write(
        '''
        Aquí se corre  pyVHR

        ''',
        pd.DataFrame({'Patient Name':["User"],'Lastname':["LastnameUser"],'Vitals':["10 bpm"]})
        
    )



