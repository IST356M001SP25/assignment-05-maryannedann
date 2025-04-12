import pandas as pd
import streamlit as st
import pandaslib as pl


# Load survey and states data
survey_data = pd.read_csv('cache/survey.csv')
states_data = pd.read_csv('cache/states.csv', header=0)

# Clean column names in both datasets (remove whitespace, line breaks)
survey_data.columns = survey_data.columns.str.strip()
states_data.columns = states_data.columns.str.strip().str.replace('\n', ' ')

# Preview column names to verify
st.write("Survey Data Columns:", survey_data.columns)
st.write("States Data Columns:", states_data.columns)

# Add cleaned country column
survey_data['_country'] = survey_data['What country do you work in?'].apply(pl.clean_country_usa)

# Filter U.S. data only
survey_data_usa = survey_data[survey_data['_country'] == 'United States']

