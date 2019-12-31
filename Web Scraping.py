#!/usr/bin/env python
# coding: utf-8

# ### Importing necessary libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Parsing url data using BeautifulSoup

# In[23]:


url ='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
html = urlopen(url)
soup=BeautifulSoup(html,'lxml')
type (soup)


# ### Convert html table data to dataframe

# In[24]:


dfs = pd.read_html(str(soup))  #returns a list of dataframes
df=dfs[0]         #we're interested in the first (and only) dataframe
df.describe()


# ### Checking for "Not assigned" borough values

# In[25]:


df.Borough.value_counts()


# ### Dropping rows with no assigned borough

# In[27]:


df=df[df.Borough!='Not assigned']
df.describe()  #verify that 77 rows have been deleted


# ### Checking for "Not assigned" neighborhood values

# In[16]:


df.loc[(df['Neighborhood']=='Not assigned')]


# ### Replacing "Not assigned" neighborhood values with corresponding borough

# In[28]:


df['Neighborhood'].replace('Not assigned',df['Borough'],inplace=True)
df.loc[(df['Neighborhood']=='Not assigned')]  #verify that all "not assigned' values have been removed


# ### Combining rows with same postcode and borough

# In[30]:


df_grouped=pd.DataFrame(df.groupby(['Postcode','Borough'])['Neighborhood'].apply(lambda x:', '.join(x)))
df_grouped.reset_index(inplace=True)
df_grouped.head()


# In[31]:


df_grouped.describe()


# In[32]:


df_grouped.shape

