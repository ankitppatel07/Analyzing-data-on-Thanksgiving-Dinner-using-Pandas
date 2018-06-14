
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
data = pd.read_csv("thanksgiving.csv", encoding = "Latin-1")
print(data.head(5))


# In[2]:


print(data.columns)


# In[3]:


series1 = data["Do you celebrate Thanksgiving?"]
print(series1.value_counts())


# In[19]:


series2 = data[data["Do you celebrate Thanksgiving?"] == "Yes"]
print(series2)


# In[10]:


series3 = data["What is typically the main dish at your Thanksgiving dinner?"]
print(series3.value_counts())


# In[9]:


series4 = data[data["What is typically the main dish at your Thanksgiving dinner?"]=="Tofurkey"]
print(series4["Do you typically have gravy?"])


# In[28]:


apple_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])
no_pies = apple_isnull & pumpkin_isnull & pecan_isnull
print(no_pies)
print(no_pies.value_counts())


# In[21]:


def conv_numeric(x):
    list1 = []
    #for x in age_series:
    if pd.isnull(x):
        return None
    list1 = x.split(" ")
    age_value = list1[0]
    age_value = age_value.replace("+", "")
    age_value = int(age_value)
    return age_value

series5 = data["Age"]
data["int_age"] = series5.apply(conv_numeric)
print(data["int_age"].describe())


# In[33]:


#FINDINGS:
#Max value is 60, whereas there can be people with ages above 60. 
#This is because we took the first element of the string.
#This make our calculations roughly approx.


# In[12]:


def conv_salary_numeric(y):
    list2 = []
    #for x in age_series:
    if pd.isnull(y):
        return None
    list2 = y.split(" ")
    age_value = list2[0]
    if age_value == "Prefer":
        return None
    age_value = age_value.replace("$", "")
    age_value = age_value.replace(",", "")
    age_value = int(age_value)
    return age_value

series6 = data["How much total combined money did all members of your HOUSEHOLD earn last year?"]
data["int_income"] = series6.apply(conv_salary_numeric)
print(data["int_income"].describe())


# In[37]:


#FINDINGS:
#Similar to the above scenario. 
#This is because we took the first element of the string.
#This make our calculations roughly approx.


# In[14]:


income_less = data[data["int_income"] < 150000]
income_less_and_travel = income_less["How far will you travel for Thanksgiving?"]
print(income_less_and_travel.value_counts())


# In[15]:


income_more = data[data["int_income"] > 150000]
income_more_and_travel = income_more["How far will you travel for Thanksgiving?"]
print(income_more_and_travel.value_counts())


# In[16]:


#FINDINGS:
#People with >150000 income celebrate thanksgiving at their home
#People with <150000 income travel to celebrate thanksgiving


# In[23]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_age"
)


# In[24]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)


# In[ ]:


#FINDINGS
#Young people attend a Friendsgiving, 
#and meet friends on Thanksgiving.

