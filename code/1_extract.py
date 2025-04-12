import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
  
# URLs for survey data and state abbreviations data
survey_url = "https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv"
states_url = "https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv"

# Extract the survey data
survey_df = pd.read_csv(survey_url)
# Extract the state abbreviations data
states_df = pd.read_csv(states_url)

# Display the first few rows of both datasets
st.write("Survey Data Sample", survey_df.head())
st.write("States Abbreviations Sample", states_df.head())

# Optionally, save the data locally for debugging purposes
survey_df.to_csv('survey_data.csv', index=False)
states_df.to_csv('states_abbr.csv', index=False)

st.write("Data has been extracted and saved.")

import os
import requests

# URL for the API or data source
data_url = "https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv"  # Replace with the actual URL

# Create 'cache' directory if it doesn't exist
if not os.path.exists('cache'):
    os.makedirs('cache')

# Send a GET request to download the file
response = requests.get(data_url)

# Save the content to the 'cache' folder
with open('cache/col_2023.csv', 'wb') as file:
    file.write(response.content)

# Verify the file is saved
print("File downloaded and saved as 'cache/col_2023.csv'")

import os
import requests

# URLs for the API or data sources (replace these with the actual URLs for 2024 and 2025)
data_url_2024 = "https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv"  # Replace with the actual URL for 2024
data_url_2025 = "https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408793&format=csv"  # Replace with the actual URL for 2025

# Create 'cache' directory if it doesn't exist
if not os.path.exists('cache'):
    os.makedirs('cache')

# Download and save the 2024 data
response_2024 = requests.get(data_url_2024)
with open('cache/col_2024.csv', 'wb') as file_2024:
    file_2024.write(response_2024.content)
print("File downloaded and saved as 'cache/col_2024.csv'")

# Download and save the 2025 data
response_2025 = requests.get(data_url_2025)
with open('cache/col_2025.csv', 'wb') as file_2025:
    file_2025.write(response_2025.content)
print("File downloaded and saved as 'cache/col_2025.csv'")