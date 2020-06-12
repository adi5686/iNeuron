#!/usr/bin/env python
# coding: utf-8

# ### Assignment 2 Tasks
# 
# 1. Create the below pattern using nested for loop in Python.
# 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# 
# 2. Write a Python program to reverse a word after accepting the input from the user.
# Input word: ineuron
# Output: norueni

# In[28]:


#1
depth = input('Enter depth of pyramid in odd number:')
depth = int(depth)
for i in range(1,depth):
    if i<(depth/2):
        for j in range(1,i):
            print('*',end='')
        print('\n')
    else:
        for j in range(0,depth-i):
            print('*',end='')
        print('\n')


# In[18]:


#2
word = input('Enter Word:')
print(word[::-1])


# In[ ]:




