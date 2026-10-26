import math

def is_square(n): 
    if n < 0:
        return False
    
    a = math.sqrt(n)
        
    if a.is_integer(): 
        return True
    else:
        return False