# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:57:45 2017

@author: B_P
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#importing dataset

dataframe = pd.read_csv('Position_Salaries.csv')
x = dataframe.iloc[ : , 1:2].values
y = dataframe['Salary'].values

from sklearn.linear_model import LinearRegression

linreg1 = LinearRegression()
linreg1.fit(x, y)

from sklearn.preprocessing import PolynomialFeatures

polreg = PolynomialFeatures(degree=10)
x_poly = polreg.fit_transform(x)
linreg2 = LinearRegression()
linreg2.fit(x_poly, y)

x_grid = np.arange(min(x), max(x)+0.3, 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color='red')
plt.plot(x_grid, linreg2.predict(polreg.fit_transform(x_grid)), color='blue')
plt.title('True or bluff')
plt.xlabel('x')
plt.ylabel('y')
plt.show()