#!/usr/bin/env python
# coding: utf-8

# 4) Session 4 Prompt: Write a Python program that declares a class describing your favorite animal. Have the data members of the class represent the following physical parameters of the animal: length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). Write an initialization function that sets the values of the data members when an instance of the class is created. Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
# 

# In[15]:


class Beaver:
    def __init__(self, arm_length=2.75, leg_length=6.5, num_eyes=2, has_tail=True, is_furry=True):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("\nFavorite animal: Beaver")
        print(f"Arm length: {self.arm_length} inches")
        print(f"Length of legs: {self.leg_length} inches")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry: {'Yes' if self.is_furry else 'No'}")

my_beaver = Beaver()
my_beaver.describe()


# In[ ]:




