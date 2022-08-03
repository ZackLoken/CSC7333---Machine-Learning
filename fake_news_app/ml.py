import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


model.fit(df[['sepal_length','sepal_width']], df[['species']])
pickle.dump(model, open('model.pkl', 'wb'))