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

# 2. Matrix Inversion 
'''use `np.linalg.inv(matrix)`'''
A = np.array([[1, 2], [3, 4]])
inverse_A = np.linalg.inv(A)
print('inverse of matrix')
print(inverse_A)

# 3. Determinant
A = np.array([[1, 2], [3, 4]])
determinant_A = np.linalg.det(A)
print("determinant") 
print(determinant_A)

#eigne value and eigen vector
A = np.array([[1, 2], [2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

#solving the linera equqtions
A = np.array([[2, 3,4], [1, -1,-2],[1,1,1]]) #in the form of [x,y,z]
b = np.array([8, -1,5])

x = np.linalg.solve(A, b)
print("solution of  A and b",x)

