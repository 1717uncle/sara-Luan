#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Data for global Amazon Prime subscribers
years = [2018, 2019, 2021]
subscribers = [100, 150, 200]  # in millions

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(years, subscribers, marker='o')
plt.title('Global Amazon Prime Subscribers (2018-2021)')
plt.xlabel('Year')
plt.ylabel('Subscribers (Millions)')
plt.grid(True)
plt.xticks(years)
plt.tight_layout()
plt.show()


# In[3]:


# Data for US Amazon Prime subscribers
years_us = list(range(2013, 2026))
subscribers_us = [
    25, 40, 54, 65, 99.7, 112.1, 124, 146.1, 
    159.8, 163.5, 167.2, 171.8, 176.2
]  # in millions

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years_us, subscribers_us, marker='o', color='orange')
plt.title('US Amazon Prime Subscribers (2013-2025)')
plt.xlabel('Year')
plt.ylabel('Subscribers (Millions)')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[4]:


# Data for Amazon Prime Day sales
years_pd = list(range(2015, 2024))
sales = [
    0.9, 1.52, 2.41, 4.19, 7.16, 10.4, 11.2, 
    12, 12.9
]  # in billions

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years_pd, sales, marker='o', color='green')
plt.title('Amazon Prime Day Sales (2015-2023)')
plt.xlabel('Year')
plt.ylabel('Sales (Billions)')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[5]:


# Data for best-selling items
items = ['Fire TV Stick', 'Lip Glowy Balm', 'Apple AirPods', 'Bissell Little Green']
quantities = [375, 375, 375, 375]  # in millions

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=quantities, y=items, palette='viridis')
plt.title('Best-Selling Items on Amazon during Prime Day (2023)')
plt.xlabel('Quantity Sold (Millions)')
plt.ylabel('Items')
plt.tight_layout()
plt.show()


# In[6]:


# Plotting Amazon Prime Day Sales Growth Comparison
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting Amazon Prime Day Sales
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Prime Day Sales (Billions)', color=color)
ax1.plot(years_pd, sales, marker='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Creating a bar plot for Amazon Prime Subscribers
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Subscribers (Millions)', color=color)
ax2.plot(years, subscribers, marker='s', color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Adding titles and legends
plt.title('Amazon Prime Day Sales Growth Comparison (2015-2023)')
fig.tight_layout()
plt.grid(True)
plt.show()


# In[7]:


# Data for Amazon Prime revenue
years_rev = list(range(2014, 2023))
revenue = [2.76, 4.47, 6.39, 9.72, 14.17, 19.21, 25.21, 31.77, 35.22]  # in billions

# Plotting Amazon Prime Revenue Trend
plt.figure(figsize=(10, 6))
plt.plot(years_rev, revenue, marker='o', linestyle='-', color='purple')
plt.title('Amazon Prime Revenue Trend (2014-2022)')
plt.xlabel('Year')
plt.ylabel('Revenue (Billions)')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[8]:


# Data for Amazon Prime Video viewers by country
countries = ['United States', 'India', 'Germany', 'United Kingdom', 
             'Japan', 'Canada', 'France', 'Australia']
viewers = [157.1, 59.8, 30.8, 22.1, 15.6, 13.9, 13.1, 4.4]  # in millions

# Plotting Amazon Prime Video Viewers by Country
plt.figure(figsize=(10, 6))
sns.barplot(x=viewers, y=countries, palette='coolwarm')
plt.title('Amazon Prime Video Viewers by Country (2023)')
plt.xlabel('Viewers (Millions)')
plt.ylabel('Country')
plt.tight_layout()
plt.show()


# In[ ]:




