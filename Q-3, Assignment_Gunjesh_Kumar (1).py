#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
def generate_random_timeseries_data(proportion_to_delete=0.2):
    # Create a date range for the year 2020,  + 20 business days 
    date_range = pd.date_range(start='2020-01-01', end='2021-01-20', freq='B')  # 'B' for business day frequency

    # Generate random data for each business day
    random_data = np.random.rand(len(date_range))

    # Create a DataFrame with the date and the generated random data
    timeseries_data = pd.DataFrame({'Date': date_range, 'Value': random_data})

    # Randomly delete some observations based on the given proportion
    num_observations_to_delete = int(proportion_to_delete * len(timeseries_data))
    indices_to_delete = np.random.choice(timeseries_data.index, num_observations_to_delete, replace=False)
    timeseries_data.drop(indices_to_delete, inplace=True)

    return timeseries_data


# In[6]:


data=generate_random_timeseries_data()
data.shape


# In[7]:


data.head(25)


# In[8]:


data['Date_Integer'] = (data['Date'] - data['Date'].min()).dt.days
data


# In[15]:


import math
def returns(data):
    tnn = {}
    for i in range(len(data)-20):
        diff = []
        Dt = data.Date.iloc[i]
        for j in range(i+1,len(data)):
            Dt_1 = data.Date.iloc[j]
            diff.append((Dt_1-Dt).days)
        minimise=abs((10/np.array(diff))-1)
        tnn[i]=i+np.argmin(minimise)
    return tnn

ten_days_return = returns(data)
print(ten_days_return)


# In[19]:


final_ret={}
for dt,dt1 in data.items():
    final_ret.append(np.log(data.Value.iloc[dtdash]/data.Value.iloc[dt])*((10/(dtdash-dt))**0.5)
               
print(final_ret)


# In[ ]:




