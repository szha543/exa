#!/usr/bin/env python
# coding: utf-8

# Import libraries and read 
# 

# In[1]:


import pandas as pd

import html5lib

get_ipython().system('pip install lxml')

wiki_url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'


result = pd.read_html(wiki_url)

df = pd.DataFrame(result[0])

df.head()


# In[2]:


#df1=df.groupby('Postal Code').reset_index()
df1 = df.groupby(['Postal Code','Borough'], as_index=False, sort=False,).sum()
df1.head()


# In[3]:


#df1["Neighborhood"].replace({'NaN','1', inplace=True)
#df1['Neighborhood ']=df1['Neighbourhood'].replace('0', df1['Borough'])
#df2=df.Neighborhood.replace({'Neighborhood':'0'},(df1['Borough']) )
#df2

#df1['Neighbourhood']=df1['Neighbourhood'].replace('0', 'Not assigned')

#df1["Neighbourhood"].replace(0,1, inplace=True)
#df1
#df1[0:1,‘Postal Code’]
#nei=df1.ix[0,"Neighborhood"]
#nei

df1.loc[df['Borough']=="Not assigned", "Neighborhood"] = df["Borough"]


#df['Neighbourhood']=df['Neighbourhood'].replace('Not assigned', df['Borough'])


#df1.loc[df["Neighbourhood"] == ("0"), "Neighbourhood"] = df["Borough"]
#df1.loc[df['Neighbourhood'] == ('Not assigned'), 'Neighbourhood'] = df['Borough']


# In[4]:


df1


# In[5]:



get_ipython().system('conda install -c conda-forge geocoder -y')


# In[11]:





def get_geocoder(postal_code_from_df):
     # initialize your variable to None
    lat_lng_coords = None
     # loop until you get the coordinates
    while(lat_lng_coords is None):
        g = geocoder.google('{}, Sydney, Australia'.format(postal_code_from_df))
        lat_lng_coords = g.latlng
    latitude = lat_lng_coords[0]
    longitude = lat_lng_coords[1]
   





# In[15]:


get_ipython().system("wget -q -O 'Geospatial_Coordinates.csv' http://cocl.us/Geospatial_data")
print('Data downloaded!')


# In[17]:


df=pd.read_csv("http://cocl.us/Geospatial_data/Geospatial_Coordinates.csv")
df


# In[19]:


pd.merge(df1, df)


# In[ ]:




