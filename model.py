import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv('housing_df.csv')

y = df['MEDV']
x = df.drop(['MEDV'], axis=1)

