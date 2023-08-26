# let me import the required modules
import pandas
from sklearn import linear_model

# let me read csv using pandas module
df=pandas.read_csv("data.csv")


# let me read x and y as coordinates 
x=df[["Weight","Volume"]]
y=df['CO2']
regr=linear_model.LinearRegression()
regr.fit(x,y)

#let pridict the CO2 will be produced when the  Weight is  and Volume is 
pridictedc02=regr.predict([[3300,1300]])
print("CO2 will be ", pridictedc02) 
# let me print the coeficient
# print("The coeficient  will be ", regr.coef_) 