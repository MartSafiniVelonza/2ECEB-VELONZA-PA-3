#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("2ECEB MART SAFINI V. VELONZA")


# ---------------

# PROBLEM 1

# a. Load the corresponding .csv file into a data frame named cars using pandas

# In[2]:


import pandas as pd


# In[8]:


Cars = pd.read_csv('Cars.csv')


# In[34]:


Cars.head()


# In[10]:


Cars.tail()


# b. Display the first five and last five rows of the resulting cars.

# In[43]:


pd.concat([Cars.head(),Cars.tail()])


# ----------------------------

# PROBLEM 2

# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

# In[44]:


Cars.loc[1:10:2]


# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[27]:


Cars[0:1]


# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[26]:


Cars.loc[[23],['Model','cyl']]


# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[33]:


Cars.loc[[1,28,18],['Model','cyl','gear']]

