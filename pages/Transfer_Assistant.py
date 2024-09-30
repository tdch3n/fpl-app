import streamlit as st
import pandas as pd
import time

st.markdown(st.session_state.page_styling, unsafe_allow_html=True)

# st.image('images/silhouette.png')

if 'starter_selections' not in st.session_state:
    st.session_state.starter_selections = [None] * 11


st.session_state.transferable_players = st.session_state.starter_selections.copy()


st.header('Transfer Assistant')
st.write('___')
st.write('''
         Before you begin, please ensure that you have 
         entered your team on the **Select Your Team** page.
         ''')


st.write('#### Would you like to potentially find sub replacements or just starters?')
subs_in = st.checkbox('Click here for subs to be included')

if subs_in:
    if 'sub_selections' not in st.session_state:
        st.session_state.sub_selections = [None] * 4
    
    st.session_state.transferable_players += st.session_state.sub_selections.copy()


st.write('#### Are there specific players that you want to transfer out?')

specific_players = st.radio('Select an option:', ('Yes', 'No'))

if specific_players == 'Yes':
    transfer_out = st.multiselect(
        "Enter any players you want to transfer out of your team",
        options = st.session_state.transferable_players,
        help="Start typing to search for a player"
        )

    transfer_options = [player for player in st.session_state.transferable_players if player in transfer_out]

elif specific_players == 'No':
    no_transfer = st.multiselect(
        "Enter any players you definitely want to keep in your team",
        options = st.session_state.transferable_players,
        help="Start typing to search for a player"
        )

    transfer_options = [player for player in st.session_state.transferable_players if player not in no_transfer]

st.write(transfer_options)

clicker = st.button(
    'DO NOT CLICK'
    )

def calculate_optimal_transfers(df):
    time.sleep(3)
    
    return df.head(5)

if clicker:
    with st.spinner('Calculating optimal transfers...'):
        loading_gif = st.image('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWNldmVxMnlwdDd5emIwMDF4NzVjejY3dWQxa2xzMDBzbWF5MGJ2eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JIX9t2j0ZTN9S/giphy.gif', width=500)
        optimal_transfers_df = calculate_optimal_transfers(st.session_state.df)
        loading_gif.empty()
    
    st.success('Optimal transfers calculated!')
    st.table(optimal_transfers_df)