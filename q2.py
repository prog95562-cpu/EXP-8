#wap for Data Types and structres in Numpy.
import numpy as np

# Data types in NumPy
a = np.array([10, 20, 30], dtype=np.int32)
b = np.array([1.5, 2.5, 3.5], dtype=np.float64)
c = np.array([True, False, True], dtype=np.bool_)

print("Integer Array:", a)
print("Data Type:", a.dtype)

print("\nFloat Array:", b)
print("Data Type:", b.dtype)

print("\nBoolean Array:", c)
print("Data Type:", c.dtype)

# Data structures in NumPy

# 1-D array
arr1 = np.array([1, 2, 3, 4, 5])
print("\n1-D Array:")
print(arr1)

# 2-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D Array:")
print(arr2)

# 3-D array
arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])
print("\n3-D Array:")
print(arr3)

