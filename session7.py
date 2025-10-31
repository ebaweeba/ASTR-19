#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
x

def my_exp(x):
    return np.exp(x)

y = my_exp(x)
plt.plot(x, y, label='exp(x)')
plt.xlabel('time [milliseconds]')
plt.ylabel ('awesomeness')
plt.title('exponential awesomeness growth')
plt.legend()
plt.grid(True)

plt.savefig("exp_plot.pdf")
plt.show()


# In[ ]:




