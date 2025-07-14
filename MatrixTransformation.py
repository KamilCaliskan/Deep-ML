try:
    # Convert inputs to NumPy arrays
    A_np = np.array(A, dtype=float)
    T_np = np.array(T, dtype=float)
    S_np = np.array(S, dtype=float)
    
    # Check if all matrices are square and same size
    if A_np.shape != T_np.shape or A_np.shape != S_np.shape:
        return -1
    
    # Check if T and S are invertible
    if np.linalg.det(T_np) == 0 or np.linalg.det(S_np) == 0:
        return -1
    
    # Compute T⁻¹
    T_inv = np.linalg.inv(T_np)
    
    # Compute T⁻¹ A S
    transformed = T_inv @ A_np @ S_np
    
    # Convert back to list of lists
    return transformed.tolist()
    
except np.linalg.LinAlgError:
    # Catches inversion failures
    return -1
except:
    # Catches any other unexpected errors
    return -1
