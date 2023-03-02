import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)
print("the type of np array a is: " + str(type(a)))
#size 
print("the size module of array a returns: " + str(a.size))
#ndim returns the dimensions
print("the dimensions of array a are: " + str(a.ndim))
#shape module returns the number of sub arrays and the size of each sub array
print("shape module: " + str(a.shape))

#numpy for vectors 
# vector addition
u = np.array([1, 0, 0])
v = np.array([0, 1, 0])
y = u + v

print("this is y and u respectively")

print(y)
print(u)

print("1d element multiplication: " + str(y * 7))

print("1d element addition: " + str(y + 3))

#npArr.max, npArr.mean
# trig math: npArr.sin(x), 
print(np.linspace(-1, 1, 4))

#print(u*y)

print(np.dot(u, y))

#each value in a 2d array is a new row
#matrix operations are the same as 1d arrays

#matrix multiplication needs to have identical array sizes - dot product (multiply all corresponding values and add) of 
# i row of first matrix and j column of second matrix

fo = np.array([1, 2, 3])
ba = np.array([4, 5, 6])

print(np.dot(fo, ba))

ye = np.array([[1, 2], [2, 3]])
ma = np.array([[1, 3], [4, 2]])

print(np.dot(ye, ma))

#np.arange(x, y, z) //creates an array with all values in specified range and increment

#np.random.permutation(np.arange(x, y)) //randomizes the order of an array
#np.random.randint(x, y)
#np.random.rand(x, y) //creates multidimensional arrays with specified dimensions

#np.array.reshape(x, y) //creates a matrix with specified rows and columns