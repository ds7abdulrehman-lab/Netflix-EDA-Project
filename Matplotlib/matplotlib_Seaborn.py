import pandas as pd
import numpy as np
df = pd.read_csv('data/Amazon.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df['Category'].value_counts())
print(df['PaymentMethod'].value_counts())
print(df['State'].value_counts())
df['FinalAmount'] = df['TotalAmount']-df['Discount']+df['ShippingCost']+df['Tax']

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Month']= df['OrderDate'].dt.month
df['Year'] = df['OrderDate'].dt.year

total_revenue = df['FinalAmount'].sum()
print('The total revenue is ', total_revenue)
total_sale_cat = df.groupby('Category')['FinalAmount'].sum().sort_values(ascending=False)
print(total_sale_cat)

average_oder = df.groupby('PaymentMethod')['FinalAmount'].sum().sort_values(ascending=False) 
print(average_oder)

high_Value= df[df['FinalAmount'] > 2000]
print(high_Value.head(10))
elect_cal = df[(df['Category']=='Electectronics') &(df['State'] =='Callifornia')]
print(elect_cal.head())