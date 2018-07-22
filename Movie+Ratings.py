
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[3]:

movies = pd.read_csv('/home/mitalideshpande/Movie-Ratings.csv')


# In[4]:

movies.head()


# In[5]:

movies.columns


# In[6]:

movies.columns = ['Film', 'Genre', 'CriticsRatings', 'AudienceRatings',
       'BudgetMillions', 'ReleaseYear']


# In[7]:

movies.info()


# In[12]:

# Convert variables into categorial variables
movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.ReleaseYear = movies.ReleaseYear.astype('category')


# In[13]:

movies.info()


# In[26]:

# Creating plots 
# Jointplots
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[27]:

jt = sns.jointplot(data=movies, x='CriticsRatings', y='AudienceRatings', kind='hex')


# In[30]:

h1 = plt.hist(movies.CriticsRatings, bins=15)


# In[41]:

#Stacked Histograms
plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions, bins=15)
plt.hist(movies[movies.Genre == 'Action'].BudgetMillions, bins=15)
plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions, bins=15)
plt.show()


# In[37]:

movies.Genre.cat.categories


# In[45]:

# adding all genres in list
list1 = [movies[movies.Genre == 'Drama'].BudgetMillions , movies[movies.Genre == 'Action'].BudgetMillions]
plt.hist(list1, bins=10, stacked=True)
plt.show()


# In[56]:

# instead of manually typing we can loop over the categories
list_gen = list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    list_gen.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)
    
plt.hist(list_gen, bins=30, stacked=True, rwidth=1, label=mylabels)
plt.legend()
plt.show()


# In[ ]:



