#!/usr/bin/env python
# coding: utf-8

# Create a Jupyter notebook, import matplotlib. Write cells that create an array x ranging from [0,1] in 100 steps and that defines functions that return sin(x) and cos(x). In a new cell use to create a multipanel plot (1 row, 2 columns), plotting sin(x) vs. x in the left panel and cos(x) vs. x in the right panel. Label the panels with sin(x) and cos(x), and save the figure as a PDF.

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace (0, 1, 100)
x

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

y_sin = sin(x)
y_cos = cos(x)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x,y_sin)
axs[0].set_title('sin(x)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('sin(x)')

axs[1].plot(x, y_cos)
axs[1].set_title('cos(x)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('cos(x)')

plt.savefig("session_8.pdf", bbox_inches="tight", facecolor="white")
plt.show()


# In[ ]:




