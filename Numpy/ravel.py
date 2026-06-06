import numpy as np
a_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(a_2d)
raveled_a = a_2d.ravel()
print(raveled_a)
raveled_a[0] = 10
print(raveled_a)
print(a_2d)
