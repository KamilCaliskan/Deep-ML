#Write a Python function that computes the dot product of a matrix and a vector
#The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible
#A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector 
#For example, an n x m matrix requires a vector of length m


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float] | int:
    if not a or not b:
        return -1
    cols_in_a = len(a[0])
    if cols_in_a != len(b):
        return -1
    result = []
    for row in a:
        if len(row) != cols_in_a:
            return -1
        dot_product = sum(row[i] * b[i] for i in range(cols_in_a))
        result.append(dot_product)
    return result
