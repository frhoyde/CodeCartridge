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
#sort
print(np.sort([3,2,1]))
#concatenate
a = np.arange(4)
b = np.arange(4)
print(np.concatenate((a,b)))

print("a.ndim " + str(a.ndim))
print("a.size " + str(a.size))
print("a.shape " + str(a.shape))
#Reshape
c = np.arange(12)
print(np.reshape(c, (3,4)))
#1D array to 2D
a = np.arange(10)
#Row Vector
rowV = a[np.newaxis, :]
print(rowV)
print(rowV.shape)
#col Vector
colV = a[: ,np.newaxis]
print(colV)
print(colV.shape)
#expand_dims
#adds an axis at pos 1
a = np.arange(10)
a = np.expand_dims(a, axis=1)
print(a)
print(a.shape)

a = np.arange(10)
a = np.expand_dims(a, axis=0)
print(a)
print(a.shape)
