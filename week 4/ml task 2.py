import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv('House Price Prediction Dataset.csv')
df['marla'] = df['Area'] / 272.25
le = LabelEncoder()
df['location_encoded'] = le.fit_transform(df['Location'])
X = df[['marla', 'location_encoded', 'Bedrooms', 'Bathrooms']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

# User Input
marla = float(input("Enter Marla: "))
location = input("Enter Location: ")
bedroom = int(input("Enter Bedrooms: "))
bathroom = int(input("Enter Bathrooms: "))
location_encoded = le.transform([location])[0]
new_house = pd.DataFrame({
    'marla': [marla],
    'location_encoded': [location_encoded],
    'Bedrooms': [bedroom],
    'Bathrooms': [bathroom]
})
predicted_price = model.predict(new_house)

print("Predicted House Price:", round(predicted_price[0], 2))