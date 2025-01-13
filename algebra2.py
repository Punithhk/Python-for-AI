#linear transformation 
# If A of m,n and x is vector in n dimension, then Ax is new vector, x is transformed into vector Ax
# ex - stretching, reflection, rotation, projection 
import numpy as np 

matrix1 = np.array([[1,5,9],[2,7,3],[8,4,6]])
print("Streched matrix : ",np.repeat(matrix1,3,axis=1))
