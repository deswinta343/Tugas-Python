#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# membaca basis data
data = pd.read_csv("data bank.csv")

# mencetak 10 baris pertama
display(data.head(10))


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# membaca basis data
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip
plt.scatter(data['age'], data['job'])

# Menambahkan judul ke plot
plt.title("Scatter Plot")

# Menetapkan label sumbu X dan Y
plt.xlabel('age')
plt.ylabel("job")

plt.savefig("output1.jpg")

plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# membaca basis data
data = pd.read_csv("data bank.csv")

# Scatter plot with age against job
plt.scatter(data['education'], data['job'], c=data['age'], s=data['duration'])

# Menambahkan judul ke plot
plt.title("Scatter Plot")

# Menetapkan label sumbu X dan Y
plt.xlabel('education')
plt.ylabel('job')

# Menambahkan colorbar
plt.colorbar()

plt.savefig("output2.jpg")

plt.show()


# In[7]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip 
plt.plot(data['balance']) 
plt.plot(data['housing'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y Labels 
plt.xlabel('balance')
plt.ylabel('housing')

plt.savefig("output3.jpg")

plt.show()


# In[10]:


import pandas as pd 
import matplotlib.pyplot as plt


# reading the database 
data = pd.read_csv("data bank.csv")

# Bar chart with day against tip 
plt.bar(data['age'], data['job'])

plt.title("Bar Chart")

# Setting the X and Y Labels 
plt.xlabel('age') 
plt.ylabel('job')

plt.savefig("output-bar.jpg")

# Adding the Legends 
plt.show()


# In[9]:


import matplotlib.pyplot as plt 
import pandas as pd

# Reading the tips.csv file 
data = pd.read_csv('data bank.csv')

#initializing the data 
job = ['student', 'enterpreneur', 'management', 'services', 'unknown',] 
data= [20, 30, 40, 50, 60]

# plotting the data 
plt.pie(data, labels=job)

# Adding title to the plot 
plt.title("Job data")

plt.savefig("output5.jpg")

plt.show()


# In[ ]:





# In[ ]:




