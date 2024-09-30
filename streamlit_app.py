import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import base64

image_path = 'images/mesh-gradient65.png'  
image = Image.open(image_path)
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()


st.session_state.page_styling = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("data:image/jpeg;base64,{img_str}");
background-size: cover;
background-repeat: no-repeat;
height: 100vh; 
width: 100vw;  
overflow: hidden; 
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(st.session_state.page_styling, unsafe_allow_html=True)
st.title("FPL Team Assistant ⚽")

st.write('___')

st.write("Welcome to the FPL Team Assistant!")

st.write(
    "This is a tool to help with transfers and captain selection.\
        To begin, please enter your team in the 'Select Your Team'\
              page found in the sidebar."
)

st.session_state.df = pd.read_csv('data/preds_for_gw5.csv')
