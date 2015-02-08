import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model
import csv
import pandas as pd

empl_train_X_data = pd.read_csv('fixtures/empl_train_X.csv')
empl_train_Y_data = pd.read_csv('fixtures/empl_train_Y.csv')
empl_test_X_data = pd.read_csv('fixtures/empl_test_X.csv')
empl_test_Y_data = pd.read_csv('fixtures/empl_test_Y.csv')

regr = linear_model.LinearRegression()

regr.fit(empl_train_X_data, empl_train_Y_data)

print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f" % np.mean((regr.predict(empl_test_X_data) - empl_test_Y_data) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(empl_test_X_data, empl_test_Y_data))

