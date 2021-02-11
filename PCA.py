import numpy as np
#        dim1,dim2
matrix = np.matrix([
    [1, 0],
    [2, 0],
    [3, 0],
    [5, 6],
    [6, 6],
    [7, 6]])
# matrix = np.matrix([])

n = len(matrix)

# center the data by substracting the mean value for each dimension
# when drawing the PCA the center is the mean_values, e.g. here: (4,3)
mean_values = np.mean(matrix, axis=0)
print("mean values")
print(mean_values)
centered_matrix = matrix - mean_values
print("centered matrix:")
print(centered_matrix)

# calculate covariance matrix: 1/n * centered_matrix_T * centered_matrix
centered_matrix_T = np.array(centered_matrix).transpose()
matrix_multiplication_result = np.dot(centered_matrix_T, np.array(centered_matrix))
print("matrix multiplication result")
print(matrix_multiplication_result)
cov_matrix = np.true_divide(matrix_multiplication_result, n)
print("cov matrix")
print(cov_matrix)

# calculate eigenvalues
eigenval, eigenvec = np.linalg.eigh(np.matrix(cov_matrix, dtype=float))
idx = eigenval.argsort()[::-1]
eigenvalues = eigenval[idx]
eigenvectors = eigenvec[:, idx]
# eigenvalues = [ [ L1 0 ]
#                 [ 0 L2 ] ]
print("eigenvalues:")
print(eigenvalues)
print("eigenvectors:")
print(eigenvectors)

# reduce to 1-dimensional space: remove second eigenvector
U = np.round(eigenvectors[:, 0], 2)
print("U = reduced to 1 dimensional vector")
print(U)

# transform data:
Y = np.dot(centered_matrix, U)
print("transformed data Y")
print(np.array(Y).transpose())

# reconstruct original data matrix:
# Z = mean + y * U_T
Z = mean_values + np.round(np.dot(Y, np.array(U).transpose()), 2)
print("reconstructed data matrix:")
print(Z)

# first PCA => largest eigenvalue and eigenvector
# PCA: 13.21 und vec([0.57, 0.82])


