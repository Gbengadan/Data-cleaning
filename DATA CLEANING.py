#!/usr/bin/env python
# coding: utf-8

# ## DATA CLEANING IN PANDAS
# 

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_excel(r"C:\Users\DELL\Downloads\Customer Call List.xlsx")
df


# In[4]:


#First drop the duplicate
df= df.drop_duplicates()
df


# In[5]:


#drop columns thats not usefull
df = df.drop(columns ="Not_Useful_Column")
df


# In[6]:


#standardize the lastname
#df["Last_Name"]=df["Last_Name"].str.lstrip("...")
#df["Last_Name"]=df["Last_Name"].str.lstrip("/")
#df["Last_Name"]=df["Last_Name"].str.rstrip("_")
df["Last_Name"]=df["Last_Name"].str.strip("123._/")
df


# In[ ]:





# In[25]:


df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')

#use lamda to standadize the phone number
#df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10]

df["Phone_Number"] = df["Phone_Number"].apply(lambda x:str(x))
df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df["Phone_Number"]= df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])


# In[27]:


#df
#remove the nan--  and the Nan--

df["Phone_Number"]= df["Phone_Number"].str.replace('nan--', '')
df["Phone_Number"]= df["Phone_Number"].str.replace('Na--', '')
df


# In[28]:


#lets split the address 
df["Address"].str.split(',',2, expand=True)
df[["Street_Adress", "State", "Zip_Code"]]= df["Address"].str.split(',',2, expand=True)
df


# In[8]:


#drop the column Address
df = df.drop(columns ="Address")
df


# In[ ]:





# In[29]:


#lets look on to paying customer column
df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"]= df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"]= df["Paying Customer"].str.replace('No','N')
df


# In[ ]:





# In[30]:


#lets look on to Do_Not_Contact column
df["Do_Not_Contact"]= df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"]= df["Do_Not_Contact"].str.replace('No','N')
df


# In[ ]:





# In[36]:


#lets fill NaN
df=df.fillna('')
df


# In[32]:


df


# In[ ]:





# In[45]:


for x in df.index:
    if df.loc[x,"Do_Not_Contact"] =='Y':
     df.drop(x, inplace=True)
    
    
df


# In[47]:


for x in df.index:
    if df.loc[x,"Phone_Number"] =='':
     df.drop(x, inplace=True)
    
    
df


# In[48]:


for x in df.index:
    if df.loc[x,"Phone_Number"] =='--':
     df.drop(x, inplace=True)
    
    
df


# In[49]:


df.reset_index(drop=True)


# In[50]:


df.to_excel(r"C:\Users\DELL\Documents\penn state university\NewClean.xlsx")


# In[ ]:




