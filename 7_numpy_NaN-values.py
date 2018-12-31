# NaN Values

import numpy as np

a = np.array([np.nan, 0 ,1 ,2, np.nan])
print(a)

# Note: Scikit-learn does NOT accept NaN values
# - They will need to be filtered out as follows

# Check for NaN values
print(np.isnan(a))

# Filter out NaN values
# - Negate the array and apply box brackets
print(a[~np.isnan(a)])

# Alternatively set the NaN values to 0
a[np.isnan(a)] = 0
print(a)


# Notes
#
# Data, in the present and minimal sense, 
# is about 2D tables of numbers, which NumPy 
# handles very well. Keep this in mind in 
# case you forget the NumPy syntax specifics. 
# Scikit-learn accepts only 2D NumPy arrays 
# of real numbers with no missing np.nan values.
# 
# From experience, it tends to be best to change 
# np.nan to some value instead of throwing 
# away data. Personally, I like to keep track 
# of Boolean masks and keep the data shape 
# roughly the same, as this leads to fewer 
# coding errors and more coding flexibility.
