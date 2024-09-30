import streamlit as st
import pandas as pd

st.markdown(st.session_state.page_styling, unsafe_allow_html=True)

# Load all player names
player_names = list(st.session_state.df['name'].unique().copy())

st.header('Enter your team')

if 'starter_selections' not in st.session_state:
    st.session_state.starter_selections = [None] * 11
if 'sub_selections' not in st.session_state:
    st.session_state.sub_selections = [None] * 4

if None in st.session_state.starter_selections or None in st.session_state.sub_selections:
    st.write('***Please select 15 unique players***')
else:
    st.write('***Team selected***')

# Starting lineup
st.subheader('Starting 11')

for i in range(11):
    current_player = st.session_state.starter_selections[i]
    options = player_names 

    if current_player in options:
        index = options.index(current_player)
    else:
        index = None 

    player = st.selectbox(
        f'Select player {i + 1}', 
        options=options,
        index=index,  # This must be an integer
        key=f'starter_{i}',
        help="Start typing to search for a player"
    )

    # Update selections
    if player not in st.session_state.starter_selections:
        st.session_state.starter_selections[i] = player

# Subs
st.subheader('Subs')

for i in range(4):
    current_player = st.session_state.sub_selections[i]
    options = player_names

    if current_player in options:
        index = options.index(current_player)
    else:
        index = None 

    player = st.selectbox(
        f'Select player {i + 1}', 
        options=options,
        index=index,  # This must be an integer
        key=f'sub_{i}',
        help="Start typing to search for a player"
    )

    # Update selections
    if player not in st.session_state.sub_selections:
        st.session_state.sub_selections[i] = player


st.subheader('You can check your team is correct here')
# Display the selected teams
st.write("Starting 11:", st.session_state.starter_selections)
st.write("Substitutes:", st.session_state.sub_selections)