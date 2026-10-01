#wap for numpy array properties and functions.

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:")
print(arr)

# Array properties
print("\nArray Properties:")
print("Dimensions (ndim):", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Item size:", arr.itemsize)

# NumPy functions
print("\nNumPy Functions:")
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Transpose:")
print(np.transpose(arr))

# Reshape
print("\nReshaped Array:")
print(arr.reshape(3, 2))
