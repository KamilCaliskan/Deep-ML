import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    """
    Calculate eigenvalues of a 2x2 matrix and return them sorted in descending order.
    
    Args:
        matrix: 2x2 matrix as a list of lists
        
    Returns:
        List of eigenvalues sorted from highest to lowest
        
    Example:
        >>> calculate_eigenvalues([[2, 1], [1, 2]])
        [3.0, 1.0]
    """
    # Convert to NumPy array for easier calculations
    A = np.array(matrix)
    
    # Calculate trace and determinant
    trace = A[0,0] + A[1,1]
    det = A[0,0]*A[1,1] - A[0,1]*A[1,0]
    
    # Calculate discriminant
    discriminant = trace**2 - 4*det
    
    # Handle complex eigenvalues case (though real matrices have real eigenvalues)
    if discriminant < 0:
        sqrt_discriminant = np.sqrt(-discriminant) * 1j
    else:
        sqrt_discriminant = np.sqrt(discriminant)
    
    # Calculate eigenvalues using quadratic formula
    lambda1 = (trace + sqrt_discriminant) / 2
    lambda2 = (trace - sqrt_discriminant) / 2
    
    # Convert to real if imaginary part is negligible
    eigenvalues = [float(np.real(lambda1)), float(np.real(lambda2))]
    
    # Sort in descending order
    eigenvalues.sort(reverse=True)
    
    return eigenvalues
