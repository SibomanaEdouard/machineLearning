# import numpy as sibo
# import matplotlib.pyplot as chant

# x=int(input("Enter the size of list 1 : "))
# xl=[]

# for _  in range(x):
#     element=int(input("Enter element : "))
#     xl.append(element)
#     if len(xl)>=x:
#         print("The elements in the list one are : ")
#         for element in xl:
#             print(element)
          
# print("\n")

# y=int(input("Enter the size of list 2: "))
# yl=[]

# for _  in range(y):
#     element2=int(input("Enter element : "))
#     yl.append(element2)
#     if len(yl)>=y:
#         print("The elements in the list one are : ")
#         for element2 in yl:
#             print(element2)
         
# # let make the scatter graph
# if y==x:
#   chant.scatter(xl,yl)
#   chant.show()
# else:
#     print("x and y must be equal!")

import matplotlib.pyplot as plt

x = int(input("Enter the size of list 1: "))
xl = []

for _ in range(x):
    element = int(input("Enter element: "))
    xl.append(element)

print("The elements in list one are:")
for element in xl:
    print(element)

print("\n")

y = int(input("Enter the size of list 2: "))
yl = []

for _ in range(y):
    element2 = int(input("Enter element: "))
    yl.append(element2)

print("The elements in list two are:")
for element2 in yl:
    print(element2)

# Make the scatter graph
if y == x:
    plt.scatter(xl, yl)
    plt.show()
else:
    print("x and y must be equal!")
