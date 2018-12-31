# NumPy arrays
# - One type of data
# - Pre-defined shape

import numpy as np


# Set of data
a = np.arange(10)
print(a)

# Print shape of data
# - In this case it is a tuple (collection with multiple parts)
print(a.shape)

# Print dimensions
print(a.ndim)

# Reshape an array - 5 height, 2 width
b = a.reshape(5,2)
print(b)

# Print dimensions again
print(b.ndim)




