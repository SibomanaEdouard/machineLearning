import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)

x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100)/x

# plt.scatter(x,y)
# plt.show()
# let me train the model
train_x=x[80:]
train_y=y[80:]

# this is testing
test_x=x[:80]
test_y=y[:80]

# # let me diplay the trained
# plt.scatter(train_x,train_y)
# # plt.scatter(test_x,test_y)
# plt.show()

mymodel=numpy.poly1d(numpy.polyfit(train_x,train_y,4))
# r2=r2_score(train_y,mymodel(train_x))

r2=r2_score(test_y,mymodel(test_x))
print(r2)
# myline=numpy.linspace(0,6,100)

# plt.scatter(train_x,train_y)
# plt.plot(myline,mymodel(myline))
# plt.show()