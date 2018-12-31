# Arithmetic operations
#

import numpy as np

a = np.arange(10)
a = a + 1
a = a.reshape(5,2)


# Sum of all elements in an array
print(a.sum())

# Sum by row
print(a.sum(axis =1))

# Find all sums by column
print(a.sum(axis=0))

# Find mean average
# - Note: dtype of averages is 'float'
print(a.mean(axis = 0))
print(a.mean(axis = 1))
print(a.mean())
