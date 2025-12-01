import pandas as pd

df = pd.read_csv("data/Amazon.csv")

df['OrderDate'] = pd.to_datetime(df['OrderDate'])

df['Month'] = df['OrderDate'].dt.to_period('M')

import matplotlib.pyplot as plt


category_list = df['Category'].unique()
data_to_plot = [df[df['Category']==cat]['TotalAmount'] for cat in category_list]

plt.figure(figsize=(12,6))
plt.boxplot(data_to_plot, labels=category_list, patch_artist=True)
plt.title("Total Sales Amount by Category")
plt.xlabel("Category")
plt.ylabel("TotalAmount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
