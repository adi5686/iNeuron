#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Write a function to compute 5/0 and use try/except to catch the exceptions.

x = int(input())
y = int(input())

try:
    r = x/y
    #print(r)
except:
    if y==0:
        print('Can not divide by 0')
    else:
        print('Some error, please re-enter')
else:
    print(r)


# #2
# Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and 
# 
# verb is in ["Play", "watch"] and 
# 
# the object is in ["Baseball","cricket"].
# 
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# 
# subjects=["Americans ","Indians"]
# 
# verbs=["play","watch"]
# 
# objects=["Baseball","Cricket"]
# 
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# In[3]:


subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

r = []

for i in subjects:
    for j in verbs:
        for k in objects:
            r.append(i+' '+j+' '+k)
            
print(r)


# In[ ]:




