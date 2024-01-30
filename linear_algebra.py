#Linear Algebra

# 1. Matrix Multiplication
'''use `np.dot() or the @ operator for matrix multiplication'''

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = np.dot(A, B)
# or equivalently
result_alternative = A @ B

print(result)
print(result_alternative)
