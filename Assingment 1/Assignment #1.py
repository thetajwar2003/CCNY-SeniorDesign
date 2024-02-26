#!/usr/bin/env python
# coding: utf-8

# # Assingment1

# ### Import

# In[20]:


import numpy as np


# ### 1) Calculate the Equcledian Distance between two vectors

# In[23]:


def eucledianDistance(x, y):
    z = x - y
    z = z**2
    return np.sqrt(np.sum(z))
    

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
             
eucledianDistance(x, y)


# ### 2) Calculate the Manhattan Distance between two vectors

# In[29]:


def manhattanDistance(x, y):
    z = x - y
    return np.sum(np.abs(z))
    

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
             
manhattanDistance(x, y)

