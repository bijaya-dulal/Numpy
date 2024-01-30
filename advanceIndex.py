#Advanced Indexing 

#two type of indexing 

# 1. Integer indexing 
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
indices = np.array([1, 3]) #provide an index to be search

result = arr[indices]
print(result)

#for 2d 
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_indices = np.array([0, 1, 2])
col_indices = np.array([1, 2, 0])

result_2d = arr_2d[row_indices, col_indices]
print(result_2d) #this should print [2 6 7]

# 2. Boolean indexing
''' Boolean indexing involves using boolean arrays to filter elements. 
It is particularly useful when you want to select elements based on a certain condition.'''
arr = np.array([1, 2, 3, 4, 5])
condition = arr > 2 

result = arr[condition] # [3 4 5]
print(result)

#Boolean indexing is often used in combination with logical operators:
arr = np.array([1, 2, 3, 4, 5])
condition = (arr > 2) & (arr < 5)

result = arr[condition]
print("combination with logical operation",result)
