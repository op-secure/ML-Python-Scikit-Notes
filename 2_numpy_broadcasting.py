# NumPy broadcasting
#  - Stretching a smaller array over a larger array
#  - ie: scalar 1 (1D) stretched to 5 x 2 shape

import numpy as np


# Set a 2d array of numbers 1 to ten
a = np.arange(10)
a = a.reshape(5,2)
print(a)


# Add 1 to every element in an array
print(a + 1)


# Squaring an array 
print(a*a)
print(a**2)


# Adding arrays
b = a+1
a = a**2
print(a+b)


# Shape mismatches
#
# The formal broadcasting rules require that whenever 
# you are comparing the shapes of both arrays from right 
# to left, all the numbers have to either match or be one.
#
# MATCH:
# 5 x 2
# 5 x 2
#
# MISMATCH:
# 5 x 2 x 1
#     5 x 2
#
# MATCH:
# 5 x 2 x 5
# 1 x 2 x 5
#
# MISMATCH
# 1 x 5 x 2
# 1 x 2 x 5
#
# MATCH
# 5 x 1
# 1 x 5
