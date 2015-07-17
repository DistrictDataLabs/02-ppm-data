# 02-ppm-data
Summary of Problem: The goal of the project was to try to predict job growth out of several economic factors. The team worked with data from the Bureau of Labor Statistics (BLS). The team struggled to  reach their initial goal. From the BLS data, PPM gathered a small set of time-based economic variables (about 8 variables) and created a set of monthly observations dating back from 2014 to 2004. The team applied some amount of regularization to the data: converting training data values from absolute values to values relative to the mean. After finalizing their training and test data sets, the team fit these observations to a Statsmodel's Ordinary Least Squares model, a scikit-learn's linear regression model, and a scikit-learn's lasso regression model. This came up with an adjusted R-squared value of .44 after predictors were added on the training data. This was the best R-squared value of all three models and came from the Ordinary Least Squares method. Once the PPM team performed predictions using test data, their R-squared values decreased significantly. The best performing model was OLS again, with a test-set R-squared score of -0.14. They ended up going after a secondary goal which is to build a web tool that allowed you to pull one economic factor at a time from BLS and see if it correlated with job growth at all. Their idea was to have an interface that allows users to plug & play data sets from the BLS websites and apply OLS regression to measure fit. They used SQLite3 as their computational data storage and their original analysis was performed in IPython Notebook. 


# Software Architecture Diagram
![](http://i62.tinypic.com/2lm4car.jpg)

# Data Flow Diagram
![](http://i59.tinypic.com/fa1ois.jpg)

[Django docs for www/uberjobz app](https://www.djangoproject.com)
