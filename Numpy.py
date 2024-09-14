# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w1vbAXA0J6U2dZ987-9aogUctReR-ZQJ
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

Exercise_Hours = np.array([2, 5, 4, 1, 6, 3, 7, 8, 2, 5, 9, 6, 4, 7, 3, 8, 9, 1, 5, 6, 2, 3, 7, 8, 4, 5, 6, 7, 8, 5, 4, 8, 7, 9, 5, 8, 1, 5, 2, 5, 9, 7, 7, 8, 2, 5, 5, 2, 6, 7, 2, 1, 1, 3, 2, 5, 6, 9, 7, 6, 9, 8, 7, 5, 9, 3, 8, 4, 8, 1, 8, 5, 8, 8, 2, 6, 4, 7, 1, 6, 1, 1, 8, 4, 1, 6, 7, 9, 1, 8, 5, 5, 9, 3, 6, 7, 3, 9, 7, 5])
Cholesterol_Level = np.array([210, 190, 200, 220, 180, 205, 170, 165, 215, 185, 160, 175, 200, 170, 210, 160, 155, 225, 195, 180, 220, 210, 175, 165, 205, 190, 185, 175, 160, 189, 197, 164, 172, 156, 189, 164, 221, 189, 213, 189, 156, 172, 172, 164, 213, 189, 189, 213, 180, 172, 213, 221, 221, 205, 213, 189, 180, 156, 172, 180, 156, 164, 172, 189, 156, 205, 164, 197, 164, 221, 164, 189, 164, 164, 213, 180, 197, 172, 221, 180, 221, 221, 164, 197, 221, 180, 172, 156, 221, 164, 189, 189, 156, 205, 180, 172, 205, 156, 172, 189])

x = Exercise_Hours.reshape(-1, 1)
y = Cholesterol_Level

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

r2_score = model.score(x_test, y_test)
print("R2 Score:", r2_score)
coeffient = model.coef_[0]
print("Coefficient:", coeffient)
intercept = model.intercept_
print("Intercept:", intercept)

plt.scatter(x_test, y_test, color='red')
plt.plot(x_test, y_pred, color='green', linestyle = '-', linewidth = 2, label='Predicted Health')
plt.xlabel('Exercise Hours')
plt.ylabel('Cholesterol Level')
plt.title('Linear Regression Model')
plt.show()

