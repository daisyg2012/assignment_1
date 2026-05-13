import numpy as np
import matplotlib.pyplot as plt

"""complex_iterations:
    check what points are bounded in the complex plane and which diverge to inf
    
    Parameters:
    x and y range, num iterations, test_pts
        
    Returns:
    bounded and divergent points

"""

def complex_iterations(x_min, x_max,y_min, y_max, test_pts= 100, iterations = 1000):
    
    # binary grid
    x = np.linspace(x_min, x_max, test_pts)
    y = np.linspace(y_min, y_max, test_pts)
    
    X, Y = np.meshgrid(x, y)
        
    cmplx = X + 1j*Y
    # zero array
    z = cmplx * 0
    
    diverged_iterations = cmplx.real*0 + iterations
    curr = cmplx.real*0 + 1 # active point
    
    for i in range(iterations):
        
        z = curr * (z**2 + cmplx) + (1-curr)*z # z^2 + c 
        
        diverged_c = np.abs(z) > 2 # creates boolean array, checks divergence
        
        curr_diverged = diverged_c * curr
        
        diverged_iterations = (curr_diverged*i)  + (1 - curr_diverged) * diverged_iterations
        
        curr = curr * (1 - diverged_c)
        
    bounded = (diverged_iterations == iterations) # boolean
        
    return bounded, diverged_iterations

        