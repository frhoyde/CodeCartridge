import numpy as np

#Create Basic Array
a = np.array([1,2,3])
print(a)
#Fill the whole array with 0s 2 being the length or dimensions
a = np.zeros(2)
print(a)
#Same as zeros but with 1
a = np.ones(2)
print(a)
#Creating an empty array
#Reason to use empty over zeros is speed
a = np.empty(2)
print(a)
#Creating a range of Elements
a = np.arange(4)
print(a)
#arange(First Number, Last Number, step size)
a = np.arange(2, 9, 2)
print(a)
#linspace(start, stop, numOfSamples, ifEndIsInclusive, retstep, dtype, axis)
a = np.linspace(0, 10, 5)
print(a)
