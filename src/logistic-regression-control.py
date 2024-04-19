import sqlite3

import pandas as pd
import cross_val_helpers as cv_helper
import data_helpers as data_helper



# Get data
df = data_helper.get_cardiac_arrest_data()

# Filter response time - remove outliers and bad data
df = data_helper.filter_response_time(df, 25, 0)

# prepare data for model
X, y = data_helper.prepare_data(df, 'xgb')
print("Feature names:", X.columns)
# Cross validation with logistic regression
search, X_test, y_predict, y_test = cv_helper.grid_search_cv(X, y, 'xgb')

# ROC curve
# cv_helper.roc_curve(search, X_test, y_test, "ROC Curve for logistic regression (control)", "figs/features/logistic-control-roc-curve.png")

# Confusion matrix
# cv_helper.plot_confusion_matrix(search, y_test, y_predict, "Confusion matrix for logistic regression (control)","figs/features/logistic-control-confusion-matrix.png")