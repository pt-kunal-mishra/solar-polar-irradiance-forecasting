import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the dataset
data = pd.read_csv('delhi_weather_2020_2024.csv')

# Streamlit app
st.title('Solar Irradiance Forecasting')

# Input date
input_date = st.date_input('Select a date', value=datetime.today())
day_of_year = input_date.timetuple().tm_yday

# Input city
city = st.text_input('Enter city name:')

# Determine temperature based on city
def get_temperature(city):
    high_temp_cities = ['New Delhi', 'Gurugram', 'Noida', 'Faridabad', 'Bahadurgarh', 'Rohtak', 'Ghaziabad','new delhi', 'gurugram', 'noida', 'faridabad', 'bahadurgarh', 'rohtak', 'ghaziabad']
    if city in high_temp_cities:
        return 45.0
    elif city in ['Uttar Pradesh', 'Bihar', 'Maharashtra', 'Gujarat','uttar pradesh', 'bihar', 'maharashtra', 'gujarat']:
        return np.random.uniform(35, 40)
    else:
        return 20.0 

# Determine suitability for solar power plantation
suitable_for_solar = False
if city:
    temperature = get_temperature(city)
    suitable_for_solar = temperature > 42

# Display temperature and suitability message if city is provided
if city:
    st.write(f'The temperature in {city} is: {temperature:.2f}°C')
    if suitable_for_solar:
        st.success("**This place is suitable for solar power plantation.**")
    else:
        st.warning("This place may not be ideal for solar power plantation.")

# Display average temperature of past years
if st.checkbox('Show Average Temperature of Past Years'):
    st.subheader('Average Temperature of Past Years')
    avg_temp = data['Temperature'].mean()
    st.write(f'The average temperature of past years is: {avg_temp:.2f}°C')

# Display GHI values, wind speed, and relative humidity
if st.checkbox('Show GHI Values, Wind Speed, and Relative Humidity'):
    st.subheader('GHI Values, Wind Speed, and Relative Humidity')
    st.write('Average GHI Value:', data['GHI'].mean())
    st.write('Average Wind Speed:', data['Wind Speed'].mean())
    st.write('Average Relative Humidity:', data['Relative Humidity'].mean())

# Display histogram of temperature
st.subheader('Histogram of Temperature')
plt.figure(figsize=(8, 6))
sns.histplot(data['Temperature'], bins=20, kde=True)
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('Temperature Histogram')
plt.grid(True)
plt.tight_layout()
st.pyplot()

# Display other graphs
st.subheader('Other Graphs')

# Line chart
st.subheader('Line Chart')
st.line_chart(data[['Temperature', 'Dew Point']])

# Area chart
st.subheader('Area Chart')
st.area_chart(data[['Wind Speed', 'Pressure']])

# Bar chart
st.subheader('Bar Chart')
st.bar_chart(data['Relative Humidity'])
