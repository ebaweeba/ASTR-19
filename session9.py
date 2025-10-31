#!/usr/bin/env python
# coding: utf-8

# Create a Jupyter notebook, import matplotlib. Use numpy to pull 1000 random numbers distributed uniformly between [0,1]. Histogram the random numbers into 100 bins, and plot the histogram. Label your axes and save the figure as a PDF.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

x = np.random.uniform(0,1,1000)
x

plt.hist(x, bins=100)

plt.xlabel('x label') #add x label
plt.ylabel('y label') #add y label
plt.title('session 9')

plt.savefig ("histogram.pdf", bbox_inches="tight", facecolor="white")

plt.show()

