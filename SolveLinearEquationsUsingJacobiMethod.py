"""
Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b
The function should iterate n times, rounding each intermediate solution to four decimal places
and return the approximate solution x
"""
import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    
    # Input validation
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square")
    if A.shape[0] != b.shape[0]:
        raise ValueError("Dimensions of A and b don't match")
    
    # Initial guess (zero vector)
    x = np.zeros_like(b, dtype=float)
    
    # Extract diagonal and remainder matrices
    D = np.diag(np.diag(A))
    R = A - D
    
    # Main iteration loop
    for _ in range(n):
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            x_new[i] = (b[i] - np.dot(R[i], x)) / A[i,i]
        x = np.round(x_new, 4)  # Round after each iteration
        
    return x.tolist()
