import numpy as np

# Define sample data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Define the file paths
output_file = 'insert_data.txt'

# Write data to a text file
np.savetxt(output_file, data, fmt='%d', delimiter='\t')

# Read data from the text file
loaded_data = np.loadtxt(output_file, dtype=int, delimiter='\t')

# Print the loaded data
print("Loaded data:")
print(loaded_data)

"""
We use np.savetxt() to write the data array to a text file named 
insert_data.txt. We specify the format ('%d' for integers),
 and the delimiter ('\t' for tab-separated values).
"""