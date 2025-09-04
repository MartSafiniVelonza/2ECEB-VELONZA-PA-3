#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("2ECEB MART SAFINI V. VELONZA")


# -----------------------

# PROBLEM 2

# In[1]:


import pandas as pd


# In[3]:


Cars = pd.read_csv('Cars.csv')


# In[4]:


Cars.loc[1:10:2]


# In[5]:


Cars[0:1]


# In[6]:


Cars.loc[[23],['Model','cyl']]


# In[7]:


Cars.loc[[1,28,18],['Model','cyl','gear']]

