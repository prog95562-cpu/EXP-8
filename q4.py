#wap for statistical operations and Broadcasting on arrays.

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original Array:")
print(arr)

# Statistical Operations
print("\nStatistical Operations")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

# Broadcasting
print("\n Broadcasting ")

# Adding a scalar to the array
print("Array after adding 10:")
print(arr + 10)

# Adding a 1-D array using broadcasting
b = np.array([10, 20, 30])

print("\nSecond Array:")
print(b)

print("\nResult after Broadcasting:")
print(arr + b)


