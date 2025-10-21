#!/usr/bin/env python
# coding: utf-8

# 6) Session 6 Prompt: Create a Jupyter Notebook where, in separate cells, you define functions that return sin(x) and cos(x).  Use Markdown cells to comment your Notebook, and describe what each function does. Create a third Python cell that will tabulate sin(x) and cos(x) using these previously defined functions vs. x, where x is tabulated between 0 and 2 with a thousand entries. Write a fourth Python cell that will use a for loop to print out the first 10 values of x, sin(x), and cos(x) in columns.
# 

# #This code defines the sine and cosine functions

# In[9]:


import numpy as np

def my_sin(x):
    return np.sin(x)

def my_cos(x):
    return np.cos(x)


# np.linspace makes an array of 1000 evenly spaced values between 0 and 2. 

# In[10]:


x = np.linspace(0, 2, 1000)
sin_values = my_sin(x)
cos_values =my_cos(x)


# this cell creates a table of how sine and cosine change as x goes from 0 to 2

# In[14]:


print("   x\t\t sin(x)\t\t cos(x)")
print("-" * 35)
for i in range(10):
    print(f"{x[i]:.5f}\t {sin_values[i]:.5f}\t {cos_values[i]:.5f}")


# In[ ]:




