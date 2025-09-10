#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("2ECEB MART SAFINI V. VELONZA")


# -----------------------

# PROBLEM 2

# In[8]:


import pandas as pd


# In[9]:


Cars = pd.read_csv('Cars.csv')


# In[14]:


Cars.iloc[:5, 1::2]


# In[11]:


Cars[0:1]


# In[12]:


Cars.loc[[23],['Model','cyl']]


# In[13]:


Cars.loc[[1,28,18],['Model','cyl','gear']]

