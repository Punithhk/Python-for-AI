import numpy as np 

colvec = np.array([[1],[4]])
print("Shape of vector ",colvec.shape,colvec)

rowvec = np.array([[1,3,4]])
zerovec = np.zeros(3)
onevec = np.ones(3)

sample = onevec.reshape(3,-1)
print("shape of vector",rowvec.shape,rowvec,zerovec,sample)
print("Element is",rowvec[0])
print("Magnitude is",np.linalg.norm(rowvec))

matrix = np.array([[1,3,89],[4,6,0]])

print("Matrix is",matrix)
#collection of matrices is called tensors, entity with >3 deminsion is a tensor
print("Element in matrix",matrix[1,1])
print("Transpose",np.transpose(matrix)) 

# diagonal, identity, symmetric, traingular matrix 
diagonalmatrix = np.diag((3,5,5))
matrix_rang = np.diag(np.arange(1,6,3))
print(diagonalmatrix,matrix_rang)
identitymatrix = np.identity(3)
print(identitymatrix)

#Symmetric matrix vs Skew symmetric matrix 
a = np.array([[3,3,1],[3,4,-1],[1,-1,1]])
transpose_a = a.transpose()
print(transpose_a)

compare = (a==transpose_a)
equal_arrays = compare.all()
print(equal_arrays)

#upper, lower triangular matrix 
ltm = np.tril([[1,4,5],[6,4,6],[9,3,5]])
utm = np.triu([[1,4,5],[6,4,6],[9,3,5]])
print(ltm,utm)

#tranpose of utm is ltm 
#vector addition
v1 = np.array([1,3,4])
v2 = np.array([3,4,6])
out = np.add(v1,v2)

#matrix add
m1 = np.array([[3,34,56],[34,56,51]])
m2 = np.array([[44,643,3],[33,54,64]])
outm = np.add(m1,m2)
print(outm)
s = 3
vector_mul = m1*s
print(vector_mul)

#inner product 
innerprod = np.inner(m1,m2)
print(innerprod)
#the dot product of identical vectors is square of magnitude of vector
# multideminsional dot single deminision 
sae = np.arange(12).reshape((3,4))
#print(sae,np.inner(sae,m1))


#orthogonal property, v1tranpose.v2 = 0
v3 = np.array([[3],[-1],[2]])
v4 = np.array([[2],[4],[-1]])
result = np.dot(np.transpose(v3),v4)
print(result)

#Angle between vectors = v1t.v2 / ||v1||.||v2||
def angle() :
    v3 = np.array([1,3,4])
    v4 = np.array([5,6,7])
    dot = np.dot(v3,v4)
    norm = np.linalg.norm(v3)*np.linalg.norm(v4)
    return np.rad2deg(np.arccos(dot/norm))

print(angle())

#Cauchy Schwarz Bunyakovsky Ineqaulity 
# if inner product of tranposev1.v2 is = to product of norms of vectors then linearly dependent 
v5 = np.array([3,-1,2])
v6 = np.array([2,6,-1])
if((np.abs(np.dot(v5.transpose(),v6)))<=np.dot(np.linalg.norm(v5),np.linalg.norm(v6))): 
    print("Linear dependent")
else:
    print("Independent")

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
colvec3 = np.array([[1],[2],[3]])
# columns of first to be equal to the rows of second matrix 
#economy of operations is m.n.q
vectorprod = np.matmul(A,colvec3)
print(vectorprod)

matrix_3x3 = np.array([1,4,5],[3,5,5],[3,5,0])
matrix1_3x3 = np.array([1,4,5],[3,5,5],[3,5,0])
result = np.dot(matrix_3x3,matrix1_3x3)
print(result)

#Adjacency matrix - info about neighbours, 2 path aparts, 
# A is adjacency matrix then A*A is used for path aparts between nodes 

# Permutation matrix 
# Identity matrix when made into matrix of type I213, I312,I231, I321 .... these are called permutation matrices of size n - n! are total of them 
# Premultiplying I213 with A result in r1 and r2 swap - I213*A
# Postmultiplying result in c1 and c2 swap - A*I213




