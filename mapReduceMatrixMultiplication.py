import pandas as pd

# matrixA = ()
# matrixB = ()

matrixA = [(1, 2, 3), (4, 5, 6)]
matrixB = [(7, 8), (9, 10), (11, 12)]


def index_matrix(matrix):
    result_matrix = []
    for row in range(0, len(matrix)):
        result_row = []
        for col in range(0, len(matrix[row])):
            row_name = row + 1
            col_name = col + 1
            result_row.append((row_name, col_name, matrix[row][col]))
        result_matrix.append(result_row)
    return result_matrix


def map_matrix_a(indexed_matrix):
    mapped_a = []
    for row in range(0, len(indexed_matrix)):
        for elem in range(0, len(indexed_matrix[row])):
            mapped_a.append((indexed_matrix[row][elem][1], ("a", indexed_matrix[row][elem][0],
                                                            indexed_matrix[row][elem][2])))
    return mapped_a


def map_matrix_b(indexed_matrix):
    mapped_b = []
    for row in range(0, len(indexed_matrix)):
        for elem in range(0, len(indexed_matrix[row])):
            mapped_b.append((indexed_matrix[row][elem][0], ("b", indexed_matrix[row][elem][1],
                                                            indexed_matrix[row][elem][2])))
    return mapped_b


def join_matrices(matrix_a, matrix_b):
    df_a = pd.DataFrame(matrix_a)
    df_b = pd.DataFrame(matrix_b)
    joined_matrix_result = pd.merge(df_a, df_b, on = [0] )
    return joined_matrix_result


def map_joined_matrix(joined_matrix):
    mapped_matrix_result = []
    for elem in range(0, len(joined_matrix)):
        mapped_matrix_result.append(((joined_matrix[elem][1][1], joined_matrix[elem][2][1]),
                                     joined_matrix[elem][1][2] * joined_matrix[elem][2][2]))
    return mapped_matrix_result


def reduce_by_key(mapped_matrix_result):
    df_mapped = pd.DataFrame(mapped_matrix_result)
    df_reduced = df_mapped.groupby(by = [0]).sum()
    return df_reduced


# index both matrixA and matrixB
indexed_matrix_a = index_matrix(matrixA)
print("indexed MatrixA:")
print(indexed_matrix_a)

print("indexed MatrixB:")
indexed_matrix_b = index_matrix(matrixB)
print(indexed_matrix_b)


# map indexed matrixA and matrixB
mapped_matrix_a = map_matrix_a(indexed_matrix_a)
print("mapped MatrixA:")
print(mapped_matrix_a)

mapped_matrix_b = map_matrix_b(indexed_matrix_b)
print("mapped MatrixB:")
print(mapped_matrix_b)


# join mapped matrixA and matrixB
joined_matrix_df = join_matrices(mapped_matrix_a, mapped_matrix_b)
print("joined MatrixA and MatrixB:")
print(joined_matrix_df)


# map joined matrixA and matrixB
mapped_matrix = map_joined_matrix(joined_matrix_df.values.tolist())
print("mapped joined matrix:")
print(mapped_matrix)


# reduce by key
reduced_result = reduce_by_key(mapped_matrix)
print("reduced by key:")
print(reduced_result)
