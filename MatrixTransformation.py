import numpy as np

def transform_matrix(A, T, S):
    try:
        A_np = np.array(A, dtype=float)
        T_np = np.array(T, dtype=float)
        S_np = np.array(S, dtype=float)
        
        if A_np.shape != T_np.shape or A_np.shape != S_np.shape:
            return -1
        
        if np.linalg.det(T_np) == 0 or np.linalg.det(S_np) == 0:
            return -1
        
        T_inv = np.linalg.inv(T_np)
        transformed = T_inv @ A_np @ S_np
        
        return transformed.tolist()
    
    except np.linalg.LinAlgError:
        return -1
    except:
        return -1
