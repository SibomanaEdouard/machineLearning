import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()
# let me read the file
df=pandas.read_csv("data.csv")
x=df[['Weight','Volume']]
scaledX=scale.fit_transform(x)
print(scaledX)