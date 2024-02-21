import numpy as np

# Create two NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Perform element-wise addition using a ufunc
result_addition = np.add(arr1, arr2)
print("Result of element-wise addition:")
print(result_addition)

# Perform element-wise multiplication using a ufunc
result_multiplication = np.multiply(arr1, arr2)
print("\nResult of element-wise multiplication:")
print(result_multiplication)

# Perform element-wise square root using a ufunc
result_sqrt = np.sqrt(arr1)
print("\nResult of element-wise square root:")
print(result_sqrt)

"""
 mathematical functions like:subtract divide power exp log sin arcsin 
 statistical: mean sum min max std 
 logical like: logical_and logical_or logical_not logical_xor
 bitwise : bitwise_and bitwise_or bitwise_not bitwise_shift 
 rounding : round floor ceil trunc

 this are the basic ufunc in numpy 
"""