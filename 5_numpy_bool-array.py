# Boolean arrays
# - Handle indexing with boolean logic

import numpy as np

a = np.arange(10).reshape(5,2) + 1

# Create a boolean array
ba = a > 5
print(ba)

# Filter by a boolean array
# Example 1
print(a[ba])

# Example 2
print(a[a < 5])
