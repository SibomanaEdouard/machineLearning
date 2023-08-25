import numpy
import math
import matplotlib.pyplot as plt
from scipy import stats
speed = [32,111,138,28,59,77,97]
x=numpy.mean(speed)
print("The mean is ", x)
print("The median is " ,numpy.median(speed))
 
# #  let calculate the mode
# print("The mode is " , stats.mode(speed))

# let me calculate standard deviation
print("The standard deviation is ",numpy.std(speed))

# let me calculate variance
"""The variance means the std square root of the std """
# python has method to handle it
variance=numpy.var(speed)
print("The variance is ",variance)
print("The std using variance is ",math.sqrt(variance))

# let me find percentile
age=[90,20,20,30,45,6,1,2,3,3,45,67,78,67,78,90,91]
print("Percentile is ",numpy.percentile(age,100))

# let me generate the random numbers 500 between 0.0 and 5.0 by using Numpy module
randomNumbes=numpy.random.uniform(0.0,5.0,1000)
# let me present the generated numbers on the histogram
plt.pie(randomNumbes)
plt.show()

# let me generate the normal 
y=numpy.random.normal(5.0,1.0,1000)
plt.hist(y,10)
plt.show()

