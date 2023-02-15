from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv('data.csv')
X = data[['feature_1', 'feature_2']]
y = data['target']
model = LinearRegression()
model.fit(X, y)
print(model.coef_)
