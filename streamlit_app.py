import streamlit as st
import pandas as pd
page_styling = """
<style>
[data-testid="stAppViewContainer"] {
background-image:  url("images/football_background1.jpg");
background-size: cover;
background-repeat: no-repeat;
}

</style>
"""

st.markdown(page_styling, unsafe_allow_html=True)
st.title("FPL Team Assistant ⚽")

st.write('___')

st.write("Welcome to the FPL Team Assistant!")

st.write(
    "This is a tool to help with transfers and captain selection.\
        To begin, please enter your team in the 'Select Your Team'\
              page found in the sidebar."
)

st.session_state.df = pd.read_csv('data/preds_for_gw5.csv')
