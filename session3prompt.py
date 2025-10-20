#!/usr/bin/env python
# coding: utf-8

# 3) Session 3 Prompt: Write a Python program that defines a function f(x) that returns x**3 + 8. In the main function of the program, call f(x) with x = 9 and print the result.  Use an if statement that executes if the result is larger than 27 and prints “YAY!”.

# In[2]:


import numpy as np
def f(x):
    result = x**3 + 8
    print (result)
    if result > 27:
        print("YAY!")

def main():
    x = np.array([9])
    f(x)

if __name__ == "__main__":
    main()


# In[ ]:




