import numpy as np
# matrix = np.array([])
matrix = np.array([[1, 1], [1, 1], [1, -1]])

# calculate svd
# U = Unitary matrix having left singular vectors as columns. Of shape (M, M) or (M, K), depending on full_matrices.
# s = singular values
# Vh = Unitary matrix having right singular vectors as rows. Of shape (N, N) or (K, N) depending on full_matrices.

U, s, Vh = np.linalg.svd(matrix)
print("unitary matrix having left singular vectors as columns:")
print(U)
print("singular values:")
print(s)
print("unitary matrix having right singular vectors as rows:")
print(Vh)

# find the SVD for the original matrix M = USigmaV_T
rows = 3
cols = 2
sigma = np.zeros((rows, cols))
print("null_sigma")
print(sigma)
np.fill_diagonal(sigma, s)
print("sigma:")
print(sigma)
reconstructed_matrix = U.dot(sigma.dot(Vh))
print("reconstrcted matrix:")
print(reconstructed_matrix)

