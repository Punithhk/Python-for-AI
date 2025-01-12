import numpy as np 

b = np.arange(0,10,3)
print(np.linspace(0,10,3))
print(np.full(5,8))
print(np.full([3,3,4],'numpy'))
print(b)
print(np.eye(3))
#identity matrix diagonal elements are 1 and other is 0 

print(np.eye)
print(np.random.rand(5))
print(np.random.randint(1,10,size=(5,3)))

x = np.random.choice([1,3,45,5,7])
print(x,type(x))