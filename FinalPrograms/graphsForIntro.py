#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import pandas as pd

database = pd.read_csv("~/researchProject/ResearchProject/a_and_e.csv")
#print(database)
col = ['blue' if n<3393 else 'black' for n in range(len(database.index))]
size = [5 if col[n]=='black' else 3 for n in range(len(col))]
fig = database.plot(kind='scatter', x='a (au)', y='e', s=size, c=col, figsize=(10,8), title='Haumea Family Objects: e vs a').get_figure()
fig.savefig('a__and_e.png')


# In[8]:


import matplotlib.pyplot as plt
import pandas as pd

database2 = pd.read_csv("~/researchProject/ResearchProject/a_and_i.csv")
#print(database)
col = ['blue' if n<3393 else 'black' for n in range(len(database2.index))]
size = [5 if col[n]=='black' else 3 for n in range(len(col))]
fig = database2.plot(kind='scatter', x='a (au)', y='i (deg)', s=size, c=col, figsize=(10,8), title='Haumea Family Objects: i vs a').get_figure()
fig.savefig('a_and_i.png')

