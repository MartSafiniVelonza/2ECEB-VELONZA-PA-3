#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("2ECEB MART SAFINI V. VELONZA")


# ----------------------------------

# PROBLEM 1

# In[7]:


import pandas as pd


# In[8]:


Cars = pd.read_csv('Cars.csv')


# In[9]:


Cars.head()


# In[10]:


Cars.tail()


# In[11]:


pd.concat([Cars.head(),Cars.tail()])

