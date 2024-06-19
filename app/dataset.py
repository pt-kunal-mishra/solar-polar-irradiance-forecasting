import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 12, 31)

# Define the list of high temperature cities including Delhi
high_temp_cities = ['New Delhi', 'Gurugram', 'Noida', 'Faridabad', 'Bahadurgarh', 'Rohtak', 'Ghaziabad']

# Initialize lists to store data
dates = []
temperatures = []
dew_points = []
wind_speeds = []
relative_humidities = []
pressures = []
precipitable_waters = []
wind_directions = []
ghis = []

# Generate data for each day
current_date = start_date
while current_date <= end_date:
    dates.append(current_date)
    temperatures.append(np.random.uniform(35, 45) if current_date.year >= 2020 else np.random.uniform(20, 30))  # Adjusted temperature for Delhi
    dew_points.append(np.random.uniform(15, 25))
    wind_speeds.append(np.random.uniform(5, 15))
    relative_humidities.append(np.random.uniform(40, 80))
    pressures.append(np.random.uniform(1000, 1020))
    precipitable_waters.append(np.random.uniform(1, 3))
    wind_directions.append(np.random.uniform(0, 360))
    ghis.append(np.random.uniform(700, 1100))
    current_date += timedelta(days=1)

# Create DataFrame
data = {
    'Date': dates,
    'Temperature': temperatures,
    'Dew Point': dew_points,
    'Wind Speed': wind_speeds,
    'Relative Humidity': relative_humidities,
    'Pressure': pressures,
    'Precipitable Water': precipitable_waters,
    'Wind Direction': wind_directions,
    'GHI': ghis
}

df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('delhi_weather_2020_2024.csv', index=False)
