#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("Downloads/100 Sales Records.csv")
df


# In[4]:


df.info()  #USE TO CHECK FOR NULL VALUES


# In[12]:


#DISPLAY COUNT OF MISSING VALUES
df.isna().sum()


# In[19]:


#USe of delimiter
df2=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Upload%20Text.txt',delimiter='\t') 
df2


# In[22]:


#IMPORTING FROM GTIHUB
#use raw data only from github
#raw button near blame button
df3=pd.read_csv('https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Upload%20CSV.csv') 
df3


# In[24]:


#drops the rows containing NULL values
df3=df3.dropna()
df3        #dropped the last row as it contained NaN value


# In[27]:


#REPLACE THE VALUES IN SPECIFIC COLUMN
df3=df3.replace({'Gender':{'Male':0,'M':0,'Female':1,'F':1}})
df3


# In[7]:


#DISPLAY ALL ROWS
pd.options.display.max_rows= None
df


# In[18]:


#DISPLAY ROWS to default 10 rows
pd.options.display.max_rows= 10
df


# In[8]:


#DISPLAY SUMMARY STATISTICS
df.describe()


# In[10]:


#DISPLAY SUMMARY STATISTIC ALL COLUMNS
df.describe(include='all')


# In[9]:


#number of unique values in df
df.nunique()


# In[11]:


#COLUMNS OF DF
df.columns


# In[13]:


#RANDOM SAMPLE OF 3 ROWS
df.sample(3)


# In[5]:


r,c=df.shape
print(df.shape)
print("rows:",r)
print("columns:",c)


# In[4]:


#first 5 rows by default
df.head()


# In[5]:


df.head(2)


# In[6]:


#last 5 rowsby default
df.tail()


# In[7]:


df[2:5]       #print 2,3,4 rows


# In[8]:


df[:]      #print every rows


# In[9]:


print(df.columns)
print(df.row)                #only columns keyword available as rows dont make sense


# In[10]:


df.Country #OR
df['Country']


# In[11]:


df[['Country','Region']]


# In[12]:


df["Unit Price"].max()


# In[13]:


df["Unit Price"].mean()        #average


# In[14]:


df["Unit Price"].std()         #standard deviation


# In[ ]:


df[['Units Sold','Unit Price','Unit Cost']].describe()


# In[ ]:


df.describe()


# In[15]:


df.index


# In[29]:


df.set_index('Item Type',inplace=True)
df


# In[30]:


df.reset_index(inplace=True)          #inplace=True edits the original dataset
df


# In[31]:


df=df[:10]
df


# In[32]:


df[['Item Type','Order ID']][df['Unit Cost']>=100]


# In[33]:


df[df['Unit Cost']>=150]


# In[36]:


df.drop_duplicates(keep='first')    #by default keep='first' means if 2 rows are
                                #same then first row will be dropped


# In[16]:


#now df is of 5 rows only
df=pd.read_csv('Downloads/100 Sales Records.csv',nrows=6)
df


# In[26]:


df=pd.read_csv('Downloads/100 Sales Records.csv',nrows=6,
na_values=['L','Offline'])
df


# In[ ]:





# In[22]:


#skipped first 2 rows
df=pd.read_csv('Downloads/100 Sales Records.csv',nrows=6,
skiprows=2) #no of rows to be skipped
df


# In[24]:


df=pd.read_csv('Downloads/100 Sales Records.csv',nrows=6,
header=1)           #make row of index 1 as header
df


# In[25]:


df


# In[30]:


df.to_csv('new.csv')    #save this file as new.csv


# In[32]:


df.to_csv('new.csv',header=None)    #removes the header


# In[34]:


df.to_csv('new.csv',header=None,index=False)


# In[ ]:




