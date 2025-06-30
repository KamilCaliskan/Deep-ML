#Reshaping a Matrix
#Matrix reshaping involves changing the shape of a matrix without altering its data
#This is essential in many machine learning tasks where the input data needs to be formatted in a specific way
#For example, consider a matrix MM:

#Input:

#a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)

#Output:

#[[1, 2], [3, 4], [5, 6], [7, 8]]

#Reshaped Matrix M′M′ with shape (4, 2):​
#Important Note:
#Ensure the total number of elements remains constant during reshaping

import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    try:
        np_array = np.array(a)
        reshaped_array = np.reshape(np_array, new_shape)
        return reshaped_array.tolist()
    except ValueError:
        return []
