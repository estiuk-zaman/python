import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
flattened_arr = arr_2d.flatten()
print(flattened_arr)
flattened_arr[0] = 10
print(flattened_arr)
print(arr_2d)