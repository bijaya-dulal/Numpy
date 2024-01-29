import numpy as np
#list
y = [1,2,3,4]
print(y)
print(type(y))
#NumPy array
x= np.array(y)
print(type(x))
print(x)

#different types of array

#creating 1D array
arr_1d = np.array([1,2,3,4])
#creating 2D array
arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
#creating 3D array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
#accessing the particular element
print(arr_3d[0,1,1])#this will access 5
#elementwise multiplication
mul_arr = arr_2d * 2

#uninitialise array
empty_arr = np.empty((3,2))
print(empty_arr)

#array filled with zero
zero_arr = np.zeros((3,3))
print(zero_arr)


#array filled with one
ones_arr = np.ones((3,3))
print(ones_arr)

#indentity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

#arrannge array (1D)
arr_range = np.arange(0, 10, 2)  # Starts from 0, stops before 10, step of 2
print(arr_range)

#Linespace
arr_linspace = np.linspace(0, 1, 5)  # 5 values evenly spaced between 0 and 1
print(arr_linspace)

#random array
random_arr = np.random.rand(2, 3)  # 2x3 array with random values between 0 and 1
print(random_arr)
