#wap for ndarray Object,Indexing and Slicing
import numpy as np

array = np.array([12,13,14,15,16,17,18,19,20])
print("Array: ",array)

#Indexing
print("find First element: ",array[0])
print("find third element: ",array[2])
print("find sixth element: ",array[5])

#Slicing
print("print elements 1-7: ",array[0:6])
print("print elements 3-8: ",array[2:9])
print("print elements 3-8: ",array[2:9:2])


