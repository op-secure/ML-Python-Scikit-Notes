# Initialising NumPy arrays and dtypes
# - Some alternatives to np.arange
# - Intro to dtypes

import numpy as np

# 1D array of zeros
a = np.zeros(10)
print(a)


# 2D array of ones
a = np.ones((5,2))
print(a)

# DataType - integer
a = np.ones((5,2), dtype = np.int)
print(a)

# Array of null values
a = np.empty(10)
print(a)

# Array of empty floating point values
a = np.empty((5,2), dtype = np.float)
print(a)
