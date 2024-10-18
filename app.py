# Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Import Dataset
df = pd.read_csv('vehicles_us.csv')

# Create a column with just manufacturer name
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Create a text header above the dataframe
st.header('Car Advertisement Data Viewer') 

# Display the dataframe with streamlit
st.dataframe(df)


# Histogram based on model year of cars based on condition
st.header('Histogram of car model year based on condition')
fig = px.histogram(df, x = 'model_year', color = 'condition')
st.write(fig)

# Histogram based on manufacturer of cars based on car type
st.header('Histogram of car manufacturers based on car type')
fig = px.histogram(df, x = 'manufacturer', color = 'type')
st.write(fig)


# Average number of days listed for cars based on the car condition
condition_dayslisted = df.groupby('condition')['days_listed'].mean()
df_condition_dayslisted = pd.DataFrame({'condition': condition_dayslisted.index, 'avg_days_listed': condition_dayslisted}).reset_index(drop=True)
# Scatterplot of average days car is listed based on the car condition
st.header('Scatterplot of average number of days cars is listed based on the car condition')
fig = px.scatter(df_condition_dayslisted, x='condition', y='avg_days_listed')
fig.update_traces(marker_size=14)
st.write(fig)
st.caption('The above scatterplot shows that most cars are listed for an average of 39 to 39.5 days, but the new cars sell the fastest and only listed for an avearage of 37 days.')

# Average number of days listed for cars based on the model year
modelyear_dayslisted = df.groupby('model_year')['days_listed'].mean()
df_modelyear_dayslisted = pd.DataFrame({'model_year': modelyear_dayslisted.index, 'avg_days_listed': modelyear_dayslisted}).reset_index(drop=True)
# Bar graph of average days listed for cars based on the model year
st.header('Bar graph of average number of days car is listed based on model year')
fig = px.bar(df_modelyear_dayslisted, x='model_year', y='avg_days_listed')
st.write(fig)
st.caption('The above bar graph shows that older cars take the longest to sell, however car models after 1994 all take an average of 40 days to sell. There are some exceptions to the older models, and some vintage cars sell very quickly.')



# Compare price distribution between car manufacturers
st.header('Compare price distribution between manufacturers')
# Get list of unique car manufacturers
manufac_list = sorted(df['manufacturer'].unique())

# Get users input from a dropdown menu
manufacturer_1 = st.selectbox(
    label = 'Select manufacturer 1',  # title of the select box
    options = manufac_list,  # options listed in the select box
    index = manufac_list.index('chevrolet')  # default pre-selected option
)

# Get user's input for the second drop down menu
manufacturer_2 = st.selectbox(
    label = 'Select manufacturer 2',
    options = manufac_list,
    index = manufac_list.index('hyundai')
)

# Filter the dataframe for these two manufacturers selected
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# Add a checkbox if user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram for car manufacturer', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# Create a plotly histogram figure of the two manufacturers price
fig = px.histogram(df_filtered, 
                   x = 'price',
                   nbins = 30,
                   color = 'manufacturer',
                   histnorm = histnorm,
                   barmode = 'overlay')
st.write(fig)


# Compare price distribution between car types
st.header('Compare price distribution between car types')
# Get list of unique car types
cartype_list = sorted(df['type'].unique())

# Get users input from a dropdown menu
type_1 = st.selectbox(
    label = 'Select Type 1',  # title of the select box
    options = cartype_list,  # options listed in the select box
    index = cartype_list.index('sedan')  # default pre-selected option
)

# Get user's input for the second drop down menu
type_2 = st.selectbox(
    label = 'Select Type 2',
    options = cartype_list,
    index = cartype_list.index('pickup')
)

# Filter the dataframe for these two manufacturers selected
mask_filter_cartype = (df['type'] == type_1) | (df['type'] == type_2)
df_filtered_cartype = df[mask_filter_cartype]

# Add a checkbox if user wants to normalize the histogram
normalize_cartype = st.checkbox('Normalize histogram for car type', value=True, key=199)
if normalize_cartype:
    histnorm = 'percent'
else:
    histnorm = None

# Create a plotly histogram figure of the two car types price
fig = px.histogram(df_filtered_cartype, 
                   x = 'price',
                   nbins = 30,
                   color = 'type',
                   histnorm = histnorm,
                   barmode = 'overlay')
st.write(fig)