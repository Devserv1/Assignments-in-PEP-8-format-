#!/usr/bin/env python
# coding: utf-8

# Question 1 

# In[1]:


import pandas as pd
df=pd.read_csv("C:/Users/JR525WA/Downloads/sales_data.csv")
df.head()


# In[2]:


missing_values=df.isna().sum()
print(missing_values)


# In[3]:


duplicate_rows=df[df.duplicated()]
print(duplicate_rows)


# In[4]:


df_zero_duplicate=df.drop_duplicates()
print(df_zero_duplicate)


# In[5]:




# Calculate and display summary statistics for 'Quantity'
quantity_mean = df['Quantity'].mean()
quantity_median = df['Quantity'].median()
quantity_std = df['Quantity'].std()

print("Summary Statistics for 'Quantity':")
print(f"Mean: {quantity_mean}")
print(f"Median: {quantity_median}")
print(f"Standard Deviation: {quantity_std}")

# Calculate and display summary statistics for 'Price'
price_mean = df['Price'].mean()
price_median = df['Price'].median()
price_std = df['Price'].std()

print("\nSummary Statistics for 'Price':")
print(f"Mean: {price_mean}")
print(f"Median: {price_median}")
print(f"Standard Deviation: {price_std}")


# In[6]:




# Calculate the total sales revenue
df['Total Revenue'] = df['Quantity'] * df['Price']

# Compute the sum of Total Revenue
total_sales_revenue = df['Total Revenue'].sum()

# Display the total sales revenue
print(f"Total Sales Revenue: {total_sales_revenue}")


# In[7]:



import matplotlib.pyplot as plt



# Create a histogram of the 'Quantity' column
plt.hist(df['Quantity'], bins=10, edgecolor='k', alpha=0.7)

# Add labels and a title to the plot
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Distribution of Sales Quantities')

# Show the histogram
plt.show()


# In[8]:




# Create a scatter plot of 'Price' vs. 'Quantity'
plt.figure(figsize=(8, 6))  
plt.scatter(df['Quantity'], df['Price'], c='blue', alpha=0.7, edgecolors='k')

# Add labels and a title to the plot
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Scatter Plot of Price vs. Quantity')

# Show the scatter plot
plt.grid(True)
plt.show()


# In[9]:




# Group the data by "Product" and compute total quantity sold and average price
grouped_data = df.groupby('Product').agg({'Quantity': 'sum', 'Price': 'mean'}).reset_index()

# Rename columns for clarity
grouped_data = grouped_data.rename(columns={'Product':'Product', 'Quantity': 'Total Quantity Sold', 'Price': 'Average Price', 'Product': 'Product'})

# Display the grouped data
print(grouped_data)


# In[10]:




# Create a bar chart for product-wise sales
plt.figure(figsize=(10, 6))  
plt.bar(grouped_data['Product'], grouped_data['Total Quantity Sold'], color='skyblue', label='Total Quantity Sold')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.title('Product-wise Sales (Total Quantity Sold)')
plt.legend()

# Show the bar chart
plt.tight_layout()
plt.show()


# In[11]:



import numpy as np
from scipy import stats



# Calculate the z-scores for the "Price" column
z_scores = np.abs(stats.zscore(df['Price']))

# Define a threshold (e.g., 2 or 3 standard deviations)
threshold = 2

# Find and print the outliers
outliers = df[z_scores > threshold]

print("Outliers:")
print(outliers)


# In[24]:


import seaborn as sns

# Create a box plot to visualize outliers in the "Price" column
plt.figure(figsize=(8, 6))  # Adjust figure size if needed
sns.boxplot(x=df['Price'], color='skyblue')

# Add labels and a title to the plot
plt.xlabel('Price')
plt.title('Box Plot of Price with Outliers')

# Show the plot
plt.show()


# In[13]:




# Convert the "Date" column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Set the "Date" column as the index
df.set_index('Order Date', inplace=True)

# Resample the data to calculate weekly sales
weekly_sales = df.resample('W').sum()

# Reset the index to have "Date" as a column again
weekly_sales.reset_index(inplace=True)

# Display the weekly sales
print(weekly_sales)


# In[14]:


# Convert the "Date" column to datetime format
weekly_sales['Order Date'] = pd.to_datetime(weekly_sales['Order Date'])

# Create a line plot to visualize the weekly sales trend
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
plt.plot(weekly_sales['Order Date'], weekly_sales['Quantity'], marker='o', linestyle='-')

# Add labels and a title to the plot
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.title('Weekly Sales Trend Over Time')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()


# Question 2

# In[15]:


df2=pd.read_csv("C:/Users/JR525WA/Downloads/supermarket_sales.csv")
df2.head()


# Q1: What does the customer rating look like and is it skewed?
# 
# Answer - Customer rating looks like Normally distributed to some extent. However, the frequency is roughly 
# similar for almost all ratings.It is also a little Right-skewed.

# In[16]:



import seaborn as sns



# Create a histogram to visualize the customer rating distribution
plt.figure(figsize=(8, 6)) 
sns.histplot(df2['Rating'], bins=10, kde=True, color='skyblue')

# Add labels and a title to the plot
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Customer Rating Distribution')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate skewness
skewness = df2['Rating'].skew()
print(f'Skewness: {skewness}')


# Q2: Is there any difference in aggregate sales across branches?
# 
# A- Yes, aggregate sale varies a little across branches. Branch A had highest sales quantity followed by C and B.

# In[17]:




# Group the data by "Branch" and compute aggregate sales
branch_sales = df2.groupby('Branch')['Quantity'].sum()

# Display the aggregate sales by branch
print(branch_sales)


# Question 3: Which is the most pouplar payment method used by customers?
# 
# A- Ewallet is the most pouplar payment method used by customers. 345 payments were made using this method.

# In[18]:




# Count the frequency of each payment method
payment_method_counts = df2['Payment'].value_counts()

# Get the most popular payment method (the one with the highest count)
most_popular_payment_method = payment_method_counts.idxmax()

# Display the most popular payment method
print(f"The most popular payment method is: {most_popular_payment_method}")
print(f"The number of payments made through this method is: {payment_method_counts.max()}")


# Q4: Does gross income affect the ratings that the customers provide?
# 
# A- The correlation corfficient of -0.036 shows that gross income negative affects customer's rating to certain extent.

# In[19]:




# Calculate the correlation coefficient between gross income and customer ratings
correlation_coefficient = df2['gross income'].corr(df2['Rating'])

# Display the correlation coefficient
print(f"Correlation Coefficient: {correlation_coefficient}")


# Q5: Which branch is the most profitable?
# 
# A- Branch 'C' is the most profitable branch. It made a profit of 5265.1765.

# In[20]:






branch_profit = df2.groupby('Branch')['gross income'].sum()

# Find the most profitable branch (the one with the highest total profit)
most_profitable_branch = branch_profit.idxmax()

# Display the most profitable branch and its total profit
print(f"The most profitable branch is: {most_profitable_branch}")
print(f"Total Profit: {branch_profit.max()}")


# Q6: Is there any time trend in gross income?
# 
# A- The graph generated by following code shows there is no discernible time trend in gross income.

# In[21]:


# Create a line plot to visualize the time trend in gross income
plt.figure(figsize=(10, 6))  
plt.plot(df2['Time'], df2['gross income'], marker='o', linestyle=' ')

# Add labels and a title to the plot
plt.xlabel('Time')
plt.ylabel('Gross Income')
plt.title('Time Trend in Gross Income')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()


# Q7: Which product line generates most income?
# 
# A- Food and Beverages generated most income. Total income is 56144.844.

# In[22]:




# Calculate total income (Sales) for each product line
product_line_income = df2.groupby('Product line')['Total'].sum()

# Find the product line with the highest total income
most_profitable_product_line = product_line_income.idxmax()

# Display the most profitable product line and its total income
print(f"The product line that generates the most income is: {most_profitable_product_line}")
print(f"Total Income: {product_line_income.max()}")


# Q8:Show the correlation between all variable.

# In[23]:




# Calculate the correlation matrix
correlation_matrix = df2.corr()

# Display the correlation matrix
print(correlation_matrix)


# In[ ]:




