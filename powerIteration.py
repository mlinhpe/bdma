import numpy as np

matrix = np.array([[14/3, 6], [6, 9]])
# matrix = np.array([])

# get unit vector for matrix
# unit_vector = []
unit_vector = [1, 0]
print("unit vector:")
print(unit_vector)

init_matrix = np.dot(matrix, unit_vector)
init_eigenvalue = np.max(init_matrix)
init_eigenvector = np.round(np.true_divide(init_matrix, init_eigenvalue), 3)
print("initial matrix:")
print(init_matrix)
print("initial eigenvalue:")
print(init_eigenvalue)
print("initial eigenvector:")
print(init_eigenvector)

counter = 0
last_eigenvalue = init_eigenvalue
eigenvector = init_eigenvector
eigenvalue = 0

while eigenvalue != last_eigenvalue:
    temp_matrix = np.dot(matrix, eigenvector)
    last_eigenvalue = eigenvalue
    eigenvalue = np.max(temp_matrix)
    eigenvector = np.round(np.true_divide(temp_matrix, eigenvalue), 3)
    counter += 1

    print("eigenvalue:")
    print(eigenvalue)
    print("eigenvector:")
    print(eigenvector)
    print("counter")
    print(counter)

print("Nach der " + str(counter) + ". Iteration konvergiert.")

