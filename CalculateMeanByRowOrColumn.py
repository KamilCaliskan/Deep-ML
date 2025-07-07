#Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode
#The function should take a matrix (list of lists) and a mode ('row' or 'column') 
#as input and return a list of means according to the specified mode
def calculate_mean(matrix, mode):
    if not matrix:
        return []
    
    if mode == 'row':
        return [sum(row)/len(row) for row in matrix]
    elif mode == 'column':
        # Tüm satırların aynı uzunlukta olduğunu kontrol et
        row_len = len(matrix[0])
        if any(len(row) != row_len for row in matrix):
            raise ValueError("All rows must have the same length")
        return [sum(col)/len(col) for col in zip(*matrix)]
    else:
        raise ValueError("Mode must be either 'row' or 'column'")
