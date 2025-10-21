#!/usr/bin/env python
# coding: utf-8

# 5) Session 5 Prompt: Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand entries. Follow the basic Python program structure, including a main program function.
# 

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

def main():
    x=np.linspace(0,2,1000)
    y=np.sin(x)

    plt.plot(x, y)
    plt.title("sin(x) vs x")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()


# In[ ]:




