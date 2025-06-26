#Write a Python function convert_range that shifts and scales the values of a NumPy array 
#from their original range [a,b][a,b] (where a=min⁡(x)a=min(x) and b=max⁡(x)b=max(x)) to a new target range [c,d][c,d]
#Your function should work for both 1D and 2D arrays, returning an array of the same shape, 
#and only use NumPy. Return floating-point results,
#and ensure you use the correct formula to map the input interval to the output interval.

import numpy as np

def convert_range(x, c, d):
    a = np.min(x)
    b = np.max(x)
    if a == b:
        # All elements are the same, map to midpoint of [c, d]
        return np.full_like(x, (c + d) / 2, dtype=np.float64)
    else:
        # Apply the transformation formula
        return c + (d - c) * (x - a) / (b - a)
