# Indexing
# - Look up values

import numpy as np

a = np.arange(10)
a = a.reshape(5,2)
print(a)


# Lookup specific value
# - Y axis then X (same as drawing an array)
print(a[0,0])
print(a[4,1])


# View an entire row
print(a[0,:])


# View an entire column
print(a[:,0])


# View specific values along both axis
print(a[2:5, :])


# View the second to fourth rows only along the first column
print(a[2:5,0])
