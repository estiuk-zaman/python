import numpy as np
a = np.array([1, 2, 3])
new_a = np.delete(a,1)
print(new_a)
a_2d = np.array([[1, 2, 3], [4, 5, 6]])
new_a_2d = np.delete(a_2d,0,axis=0)
print(new_a_2d)