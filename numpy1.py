import numpy as np

#broadcasting (use to streched the smaller array to larger array to match 
# the shape of the larger array before perform operations)
a = np.array([1, 2, 3])
b = 2
result = a + b 
print(result)

# Broadcasting with arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
row_mean = arr.mean(axis=1)  # Computing the mean along the rows
print(row_mean)
row_mean_expanded = row_mean[:, np.newaxis] # Add a new axis to row_mean to make it a column vector
print(row_mean_expanded)
centered_arr = arr - row_mean_expanded# Broadcasting to subtract mean from each element
print(centered_arr)