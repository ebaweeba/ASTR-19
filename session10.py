#!/usr/bin/env python
# coding: utf-8

# Create a Jupyter notebook, import matplotlib. On the numpy website, read about the random number distributions available for pulling random variates.  Select your favorite distribution (other than uniform) and pull 1000 random numbers from that distribution. Histogram the random numbers into 100 bins, and plot the histogram. Label your axes and save the figure as a PDF.
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

x = np.random.geometric(p=0.3, size=1000)
x

plt.hist(x, bins=100, color='mediumseagreen', edgecolor='black')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('session 10 prompt: geometric distribution')

plt.savefig("geometric_distribution_histogram.pdf", bbox_inches="tight", facecolor="white")

plt.show()  

