#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


battle = pd.read_csv('battles.csv')


# In[3]:


battle.head()


# In[4]:


battle.shape


# In[5]:


battle.rename(columns={'attacker_1':'primary_attacker'},inplace=True)
battle.head()


# In[6]:


battle.rename(columns={'defender_1':'primary_defender'},inplace=True)
battle.head()


# In[7]:


battle['attacker_king'].value_counts()


# In[8]:


battle['location'].value_counts()


# In[9]:


sns.set(rc={'figure.figsize':(13,5)})
sns.barplot(x='attacker_king',y='attacker_size',data=battle)
plt.show()


# In[10]:


sns.set(rc={'figure.figsize':(13,5)})
sns.barplot(x='defender_king',y='defender_size',data=battle)
plt.show()


# In[11]:


sns.countplot(x=battle['attacker_king'],hue=battle['battle_type'])
plt.show()


# In[12]:


death = pd.read_csv('character-deaths.csv')
death.head()


# In[13]:


death.shape


# In[14]:


death['Gender'].value_counts()


# In[15]:


death['Nobility'].value_counts()


# In[16]:


sns.countplot(death['Death Year'])
plt.show()


# In[ ]:




