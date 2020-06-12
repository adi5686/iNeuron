#!/usr/bin/env python
# coding: utf-8

# ### Assignment Tasks
# 
# 1. Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.
# 
# 2. Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.
# 
# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3
# 

# In[29]:


#1
for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        print(i, end=',')
    


# In[30]:


#2
first = input('Please Enter First Name')
last = input('Please Enter Last Name')
print(first[::-1], last[::-1])


# In[31]:


#3
dia = input('Enter Diameter in cm')
dia = int(dia)
print('Volume of the sphere is :',(4*3.14*dia*dia*dia/24))


# In[ ]:




