import streamlit as st
import pandas as pd

st.title("FPL team helper ⚽")
st.write(
    "A tool to assist with transfers and captain selection.\
        To begin, please enter your team in the sidebar."
)


# ------- Allow users to enter team --------
# Load all player names
df = pd.read_csv('data/merged_gw.csv')
player_names = df['name'].unique().copy()


# ------- Sidebar for team entry --------
st.sidebar.header('Enter your team')
starter_selections = []
sub_selections = []

# Staring lineup
st.sidebar.subheader('Starting 11')

for i in range(11):
    remaining_players = [player for player in player_names\
                          if player not in starter_selections\
                              and player not in sub_selections]

    player = st.sidebar.selectbox(
        'Enter player', 
        options = remaining_players,
        key = f'starter_{i}',
        help="Start typing to search for a player"
        )
    starter_selections.append(player)

# Subs
st.sidebar.subheader('Subs')

for i in range(4):
    remaining_players = [player for player in player_names\
                          if player not in starter_selections\
                              and player not in sub_selections]

    player = st.sidebar.selectbox(
        'Enter player', 
        options = remaining_players,
        key = f'sub_{i}',
        help="Start typing to search for a player"
        )
    sub_selections.append(player)

