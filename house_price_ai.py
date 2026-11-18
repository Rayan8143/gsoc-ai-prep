import numpy as np
from sklearn.linear_model import LinearRegression

sizes = np.array([[500], [1000], [1500], [2000], [2500]])

prices = np.array([25, 50, 75, 100, 125])

model = LinearRegression()
model.fit(sizes, prices)

new_house = np.array([[1800]])
predicted_price = model.predict(new_house)

print(f"Predicted price for 1800 sq. ft: {predicted_price[0]:.2f} lakhs")