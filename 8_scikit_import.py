import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

print(iris)

print(datasets.load_digits())

print(iris.DESCR)

print(iris.data)

# Examine shape of the data
print(iris.data.shape)

# Load the first row
print(iris.data[0])

# View collumn names
print(iris.feature_names)

# View output variable - classification
print(iris.target)
print(iris.target.shape)
print(iris.target_names)
print(iris.target[0])

# dtype string, 10 chars max
print(np.array(['setosa', 'versicolor', 'virginica'], dtype='|S10'))


# Note
#
# The iris dataset is intended to be for a supervised 
# machine learning task because it has a target array, 
# which is the variable we desire to predict from the 
# observation variables. Additionally, it is a 
# classification problem, as there are three numbers 
# we can predict from the observations, one for each 
# type of flower. In a classification problem, we are 
# trying to distinguish between categories. The 
# simplest case is binary classification. The iris 
# dataset, with three flower categories, is a multi-class 
# classification problem.



