
import numpy as np

class DimensionError(Exception):
    """Base class for exceptions in this module."""
    pass

def matrix_multiply(left, right):
    """Multply two 2D matrices, raise DimensionError if the dimensions don't match."""

    # Complete the rest of this code!
    



    return np.array([[5, 2], [3, 4]])

def user_input_matrix():
    R = int(input("Enter the number of rows:\t")) 
    C = int(input("Enter the number of columns:\t"))

    assert(R > 0), "Number of rows must be positive"
    assert(C > 0), "Number of columns must be positive"
  
    # Initialize matrix 
    matrix = [] 
    print("Enter the entries rowwise:") 
  
    # For user input 
    for i in range(R):          # A for loop for row entries 
        a = [] 
        for j in range(C):      # A for loop for column entries 
             a.append(int(input("Row %i, Column %i:\t" % (i, j)))) 
        matrix.append(a) 
        
    return np.array(matrix)

if __name__ == "__main__":
    print("Left matrix")
    print("=====================")
    left = user_input_matrix()
    print("Right matrix")
    print("=====================")    
    right = user_input_matrix()

    print("Product")
    print("=====================")    
    print(matrix_multiply(left, right))     
