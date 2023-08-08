import numpy as np
import matplotlib.pyplot as plt
from utils import *
import copy
import math

# load the dataset
x_train, y_train = load_data()

# print("Type of x_train:",type(x_train))
# print("First five elements of x_train are:\n", x_train[:5]) 

# print ('The shape of x_train is:', x_train.shape)
# print ('The shape of y_train is: ', y_train.shape)
# print ('Number of training examples (m):', len(x_train))

# x_train = number of people per city times 1000
# y_train = profit per restraunts in the city

# The goal is to find out which cities are the most profitable and predict where I should put new restraunts

