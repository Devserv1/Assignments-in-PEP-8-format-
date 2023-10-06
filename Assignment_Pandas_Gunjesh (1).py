#!/usr/bin/env python
# coding: utf-8




import pandas as pd
data = pd.read_csv("C:/Users/JR525WA/Downloads/Assignment_Pandas_Q1.csv")
df = data



df.head()


df.isna()


df.columns


# # Question 1- part(1)



df.groupby('Region')['Units'].sum()


# So, Central region is delivering maximum orders

# # Question 1- part(2)



Manager_performance=df.groupby('Manager')['Units'].sum()
Manager_performance





Manager_performance_data={'Manager': ['Douglas', 'Hermann', 'Martha', 'Timothy'],
                          'Units': [415, 647, 704, 355]}
Manager_performance_df = pd.DataFrame(Manager_performance_data)
Manager_performance_df





Manager_performance_df_sorted=Manager_performance_df.sort_values('Units',ascending=False)
Manager_performance_df_sorted





Manager_performance_df_sorted['Rank'] = ['A','B','C','D']
Manager_performance_df_sorted



df


# # Question 1- part(3)


import re

df_copy=df.copy()

cleaned_columns=df_copy.columns

def remove_special_chars(value):
    if isinstance(value, str):
        return re.sub(r'[^a-zA-Z0-9.]', '', value)
    return value

# Apply the function to the specified columns
for column in cleaned_columns:
    df_copy[column] =df_copy[column].apply(remove_special_chars)

print(df_copy)



df_copy.fillna(5)



df_copy.drop_duplicates()



df['OrderDate'] = pd.to_datetime(df['OrderDate'])
print(df)



# # Question 1- part(4)


from datetime import datetime
today = pd.to_datetime(datetime.today().date())  # Get today's date without the time
df['DaysOld'] = (today - df['OrderDate']).dt.days

print(df)


# # Question 1- part(5)


import re

df_copy_2 = df.copy()

cleaned_columns=df_copy_2.columns

def remove_special_chars(value):
    if isinstance(value, str):
        return re.sub(r'[^a-zA-Z0-9.]', '', value)
    return value

# Apply the function to the specified columns
for column in cleaned_columns:
    df_copy_2[column] =df_copy_2[column].apply(remove_special_chars)

print(df_copy_2)



df_copy_2['Sale_amt']



# Convert 'Sale_amt' to numeric, coercing non-numeric values to NaN
df_copy_2['Sale_amt'] = pd.to_numeric(df_copy_2['Sale_amt'], errors='coerce')

# Inspect and clean non-numeric values if needed
non_numeric_indices = df_copy_2[df_copy_2['Sale_amt'].isna()].index



pivot_table1 = df_copy_2.pivot_table(index='Manager', values=['Units', 'Sale_amt'], aggfunc={'Units': 'sum', 'Sale_amt': 'mean'})
print(pivot_table1)


# # Question 1- part(6)


# Filter rows where Manager is "Douglas"
douglas_data = df_copy_2[df_copy_2['Manager'] == 'Douglas']

# Create a pivot table for total sale amount region-wise, manager-wise, and salesman-wise
pivot_table2 = douglas_data.pivot_table(index=['Region', 'Manager', 'SalesMan'], values='Sale_amt', aggfunc='sum')

print(pivot_table2)


# # Question 1- part(8)

# Group by columns and sort sum of Sale_amt within each group
sorted_grouped_df = df_copy_2.groupby(['Region', 'Manager', 'SalesMan', 'Item'])['Sale_amt'].sum().reset_index().sort_values('Sale_amt', ascending=False)

print(sorted_grouped_df)


# # Question 1- part(9)


grouped_df = df_copy_2.groupby('Region').agg({
    'Manager': 'unique',
    'SalesMan': 'unique',
    'Item': 'unique'
}).reset_index()

print(grouped_df)


# # Question 1- part(10)


df_copy_2['OrderDate'] = pd.to_datetime(df['OrderDate'], dayfirst=True)

# Check if OrderDate is a business day (weekday)
df_copy_2['IsBusinessDay'] = df_copy_2['OrderDate'].dt.weekday < 5

print(df_copy_2)


# # Question 2- part(1)


pip install yfinance


import yfinance as yf
import datetime

# Define the symbols for the three companies
symbols = ['AAPL', 'GOOGL', 'META']

# Define the date range (past 10 years)
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365 * 10)

# Download historical data
data_AAPL = yf.download('AAPL', start=start_date, end=end_date, group_by='ticker')
data_GOOGL = yf.download('GOOGL', start=start_date, end=end_date, group_by='ticker')
data_META = yf.download('META', start=start_date, end=end_date, group_by='ticker')

print(data_AAPL.head())
print(data_GOOGL.head())
print(data_META.head())

data_AAPL_Closing=data_AAPL['Close']
data_GOOGL_Closing=data_GOOGL['Close']
data_META_Closing=data_META['Close']



print(data_AAPL_Closing.head())
print(data_GOOGL_Closing.head())
print(data_META_Closing.head())


# # Question 2- part(2)

import pandas as pd

# Merge DataFrames based on the 'Date' column
merged_data = pd.merge(data_AAPL_Closing,data_GOOGL_Closing, on='Date', how='outer')
final_merged_data = pd.merge(merged_data,data_META_Closing, on='Date', how='outer')


final_merged_data.rename(columns={
    'Close_x': 'AAPL_Close',
    'Close_y': 'GOOGL_Close',
    'Close': 'META_Close'
}, inplace=True)


print(final_merged_data.head())


# # Question 2- part(3)


import numpy as np



# Calculate log returns for each stock
final_merged_data['AAPL_Log_Return'] = np.log(final_merged_data['AAPL_Close'] / final_merged_data['AAPL_Close'].shift(1))
final_merged_data['GOOGL_Log_Return'] = np.log(final_merged_data['GOOGL_Close'] / final_merged_data['GOOGL_Close'].shift(1))
final_merged_data['META_Log_Return'] = np.log(final_merged_data['META_Close'] / final_merged_data['META_Close'].shift(1))


print(final_merged_data.head())


# # Question 2- part(4)



# Calculate the portfolio returns using random weights
final_merged_data['Portfolio_Return'] = (
    0.2 * final_merged_data['AAPL_Log_Return'] +
    0.4 * final_merged_data['GOOGL_Log_Return'] +
    0.4 * final_merged_data['META_Log_Return']
)

# Sort the portfolio returns
sorted_returns = final_merged_data['Portfolio_Return'].dropna().sort_values()


confidence_levels = [99, 95, 90]

# Calculate VaR for each confidence level
var_percentiles = {}  

# Loop through each confidence level and calculate VaR
for confidence in confidence_levels:
    percentile = 100 - confidence  
    var = np.percentile(sorted_returns, percentile)  
    var_percentiles[confidence] = var  
    
print(var_percentiles)



# # Question 2- part(5)


final_merged_data['AAPL_Log_Return_2'] = np.log(final_merged_data['AAPL_Close'] / final_merged_data['AAPL_Close'].shift(2))
final_merged_data['GOOGL_Log_Return_2'] = np.log(final_merged_data['GOOGL_Close'] / final_merged_data['GOOGL_Close'].shift(2))
final_merged_data['META_Log_Return_2'] = np.log(final_merged_data['META_Close'] / final_merged_data['META_Close'].shift(2))
final_merged_data['AAPL_Log_Return_5'] = np.log(final_merged_data['AAPL_Close'] / final_merged_data['AAPL_Close'].shift(5))
final_merged_data['GOOGL_Log_Return_5'] = np.log(final_merged_data['GOOGL_Close'] / final_merged_data['GOOGL_Close'].shift(5))
final_merged_data['META_Log_Return_5'] = np.log(final_merged_data['META_Close'] / final_merged_data['META_Close'].shift(5))
final_merged_data['AAPL_Log_Return_10'] = np.log(final_merged_data['AAPL_Close'] / final_merged_data['AAPL_Close'].shift(10))
final_merged_data['GOOGL_Log_Return_10'] = np.log(final_merged_data['GOOGL_Close'] / final_merged_data['GOOGL_Close'].shift(10))
final_merged_data['META_Log_Return_10'] = np.log(final_merged_data['META_Close'] / final_merged_data['META_Close'].shift(10))

print(final_merged_data.head())


# Calculate the portfolio returns using random weights
final_merged_data['Portfolio_Return_2'] = (
    0.2 * final_merged_data['AAPL_Log_Return_2'] +
    0.4 * final_merged_data['GOOGL_Log_Return_2'] +
    0.4 * final_merged_data['META_Log_Return_2']
)

final_merged_data['Portfolio_Return_5'] = (
    0.2 * final_merged_data['AAPL_Log_Return_5'] +
    0.4 * final_merged_data['GOOGL_Log_Return_5'] +
    0.4 * final_merged_data['META_Log_Return_5']
)

final_merged_data['Portfolio_Return_10'] = (
    0.2 * final_merged_data['AAPL_Log_Return_10'] +
    0.4 * final_merged_data['GOOGL_Log_Return_10'] +
    0.4 * final_merged_data['META_Log_Return_10']
)

# Sort the portfolio returns
sorted_returns_2 = final_merged_data['Portfolio_Return_2'].dropna().sort_values()
sorted_returns_5 = final_merged_data['Portfolio_Return_5'].dropna().sort_values()
sorted_returns_10 = final_merged_data['Portfolio_Return_10'].dropna().sort_values()

confidence_levels = [99, 95, 90]

# Calculate VaR for each confidence level
var_percentiles_diff_period = {}  

# Loop through each confidence level and calculate VaR
for confidence in confidence_levels:
    percentile = 100 - confidence  
    var_2 = np.percentile(sorted_returns_2, percentile)
    var_5 = np.percentile(sorted_returns_5, percentile)
    var_10 = np.percentile(sorted_returns_10, percentile)
    var_percentiles_diff_period[confidence] = var_2,var_5,var_10
    
print(var_percentiles_diff_period)


# # Question 2- part(5)


df_H1=pd.DataFrame(var_percentiles,index=['1day'])

column_names=['99 %','95 %','90 %']
df_H1.columns=column_names


print(df_H1)


df_H_diff_pd = pd.DataFrame(var_percentiles_diff_period, index=['2day','5day','10day'])

column_names=['99 %','95 %','90 %']
df_H_diff_pd.columns=column_names

print(df_H_diff_pd)


Summary_dataframe=pd.concat([df_H1,df_H_diff_pd])
print(Summary_dataframe)


# # Question 3


data1=pd.read_excel("C:/Users/JR525WA/Downloads/13-07-2023_Region_mu_sigma_1.xlsx")

data2=pd.read_excel("C:/Users/JR525WA/Downloads/14-03-2024_Region_mu_sigma_2.xlsx")
data3=pd.read_excel("C:/Users/JR525WA/Downloads/31-05-2025_Region_mu_sigma_3.xlsx")
data4=pd.read_excel("C:/Users/JR525WA/Downloads/19-08-2026_Region_mu_sigma_4.xlsx")
data5=pd.read_excel("C:/Users/JR525WA/Downloads/01-09-2027_Region_mu_sigma_5.xlsx")
data6=pd.read_excel("C:/Users/JR525WA/Downloads/14-07-2022_Region_mu_sigma_6.xlsx")
data7=pd.read_excel("C:/Users/JR525WA/Downloads/05-05-2021_Region_mu_sigma_7.xlsx")
data8=pd.read_excel("C:/Users/JR525WA/Downloads/12-07-2020_Region_mu_sigma_8.xlsx")
data9=pd.read_excel("C:/Users/JR525WA/Downloads/03-04-2019_Region_mu_sigma_9.xlsx")
data10=pd.read_excel("C:/Users/JR525WA/Downloads/01-02-2018_Region_mu_sigma_10.xlsx")
One_file=pd.concat([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10])
#print(One_file)
print(data5)




# Create the transformed dataset
transformed_data1 = []

for index, row in data1.iterrows():
    for region in ['NorthAfrica', 'SouthAfrica', 'Europe']:
        transformed_data1.append({
            'Date': '13-07-2023',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df1 = pd.DataFrame(transformed_data1)


print(transformed_df1)



transformed_data2 = []

for index, row in data2.iterrows():
    for region in ['CAN', 'CHA', 'EGY']:
        transformed_data2.append({
            'Date': '14-03-2024',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df2 = pd.DataFrame(transformed_data2)


print(transformed_df2)


transformed_data3 = []

for index, row in data3.iterrows():
    for region in ['MMR', 'MEX', 'MDV']:
        transformed_data3.append({
            'Date': '31-05-2025',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df3 = pd.DataFrame(transformed_data3)


print(transformed_df3)


transformed_data4 = []

for index, row in data4.iterrows():
    for region in ['KAZ', 'JPN', 'ITA']:
        transformed_data4.append({
            'Date': '19-08-2026',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df4 = pd.DataFrame(transformed_data4)


print(transformed_df4)



transformed_data5 = []

for index, row in data5.iterrows():
    for region in ['NA', 'Ind']:
        transformed_data5.append({
            'Date': '01-09-2027',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df5 = pd.DataFrame(transformed_data5)


print(transformed_df5)


transformed_data6 = []

for index, row in data6.iterrows():
    for region in ['SYR', 'PER', 'PAN']:
        transformed_data6.append({
            'Date': '14-07-2022',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df6 = pd.DataFrame(transformed_data6)


print(transformed_df6)


transformed_data7 = []

for index, row in data7.iterrows():
    for region in ['A', 'SA', 'Eur']:
        transformed_data7.append({
            'Date': '05-05-2021',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df7 = pd.DataFrame(transformed_data7)


print(transformed_df7)


transformed_data8 = []

for index, row in data8.iterrows():
    for region in ['NA', 'Ind', 'Eur']:
        transformed_data8.append({
            'Date': '12-07-2020',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df8 = pd.DataFrame(transformed_data8)


print(transformed_df8)


transformed_data9 = []

for index, row in data9.iterrows():
    for region in ['AUS', 'ZWB', 'Eur']:
        transformed_data9.append({
            'Date': '03-04-2019',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df9 = pd.DataFrame(transformed_data9)


print(transformed_df9)


transformed_data10 = []

for index, row in data10.iterrows():
    for region in ['SA', 'SE', 'Eur']:
        transformed_data10.append({
            'Date': '01-02-2018',
            'Rating': row['Rating'],
            'Region': region,
            'mu': row[f'{region}_mu'],
            'sigma': row[f'{region}_sigma']
        })

transformed_df10 = pd.DataFrame(transformed_data10)


print(transformed_df10)


Result_df=pd.concat([transformed_df1,transformed_df2,transformed_df3,transformed_df4,transformed_df5,transformed_df6,transformed_df7,transformed_df8,transformed_df9,transformed_df10], ignore_index=True)
print(Result_df)





