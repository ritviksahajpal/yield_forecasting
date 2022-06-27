#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
data = np.random.randn(3,100)
data[0, :10]


# In[2]:


##PLOT


# In[3]:


import matplotlib.pyplot as plt
plt.scatter(data[0],data[1],c=data[2], s=100*np.abs(data[2]))


# In[ ]:




