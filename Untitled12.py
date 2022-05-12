#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


car = pd.read_csv("2. Cars Data1.csv")


# In[5]:


#data cleaning


# In[6]:


car.head()


# In[8]:


car.shape


# In[9]:


#finding null values


# In[11]:


car.isnull().sum()


# In[17]:


car['Cylinders'].fillna(car['Cylinders'].mean(), implace = True)


# In[18]:


car


# In[19]:


#based on value counts different types of make are in the dataset


# In[20]:


car.head(2)


# In[21]:


car['Make'].value_counts()


# In[22]:


#filtering


# In[23]:


car.head(2)


# In[26]:


car[car['Origin'].isin(['Asia','Europe'])]


# In[27]:


#removing unwanted records


# In[29]:


car.head(2)


# In[33]:


car[car['Weight'] > 4000]


# In[ ]:


#applying function on column


# In[34]:


car.head(2)


# In[41]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)


# In[42]:


car


# In[ ]:




