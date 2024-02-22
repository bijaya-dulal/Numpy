import numpy as np

# Create a sample NumPy array
arr = np.arange(10)
print(arr)
# Save the array to a binary file
np.save('my_array.npy', arr)

# Load the array from the binary file
loaded_arr = np.load('my_array.npy')

# Print the loaded array
print("Loaded array:", loaded_arr)
