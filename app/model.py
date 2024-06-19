import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv('/workspaces/solar-polar-irradiance-forecasting/app/delhi_weather_2020_2024.csv')

# Split the data into features (X) and target variable (y)
X = df.drop(columns=['Date', 'GHI'])  # Excluding Date and GHI columns from features
y = df['GHI']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Train the model on the training set
model.fit(X_train, y_train)

# Predict on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# import joblib
# joblib.dump(model, 'linear_regression_model_delhi.pkl')
