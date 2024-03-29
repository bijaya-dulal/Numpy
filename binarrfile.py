import numpy as np

# Create a sample NumPy array
arr = np.arange(10)
print(arr)
# Save the array to a binary file # rewrite the file
np.save('my_array.npy', arr)

# Load the array from the binary file 
loaded_arr = np.load('my_array.npy')

# Print the loaded array
print("Loaded array:", loaded_arr)

#---------------------------************************************----------------------------------


#for multiple array in same file # it also rewrite the file
arr1 = np.arange(10)
arr2 = np.random.rand(5, 5)
arr3 = np.ones((3, 3))

# Save multiple arrays to a single file using np.savez()
np.savez('multiple_arrays.npz', arr1=arr1, arr2=arr2, arr3=arr3)

# Load the arrays from the saved file
data = np.load('multiple_arrays.npz')

# Access the loaded arrays by name
loaded_arr1 = data['arr1']
loaded_arr2 = data['arr2']
loaded_arr3 = data['arr3']
print("from multiple_arrays.npyz")
# Print the loaded arrays
print("Loaded arr1:", loaded_arr1)
print("Loaded arr2:", loaded_arr2)
print("Loaded arr2:", loaded_arr3)

#we can append the file in this way
# Create some additional sample NumPy arrays
arr4 = np.linspace(0, 1, 10)
arr5 = np.eye(4)

# Append additional arrays to the existing .npz file
with np.load('multiple_arrays.npz') as data:
    np.savez('multiple_arrays.npz', **data, arr4=arr4, arr5=arr5)

# Load the arrays from the updated file
data = np.load('multiple_arrays.npz')

# Access the loaded arrays by name
loaded_arr1 = data['arr1']
loaded_arr2 = data['arr2']
loaded_arr3 = data['arr3']
loaded_arr4 = data['arr4']
loaded_arr5 = data['arr5']
print("the appende file output")
# Print the loaded arrays
print("Loaded arr1:", loaded_arr1)
print("Loaded arr2:", loaded_arr2)
print("Loaded arr3:", loaded_arr3)
print("Loaded arr4:", loaded_arr4)
print("Loaded arr5:", loaded_arr5)
