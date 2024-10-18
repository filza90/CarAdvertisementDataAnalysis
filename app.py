# Import Libraries
import streamlit as st
import pandas as pd
import plotly_express as px

# Import Dataset
df = pd.read_csv('../vehicles_us.csv')

# Create a column with just manufacturer name
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Create a text header above the dataframe
st.header('Data viewer') 

# Display the dataframe with streamlit
st.dataframe(df)