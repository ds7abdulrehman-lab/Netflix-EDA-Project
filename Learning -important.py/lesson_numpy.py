import pandas as pd
import numpy as np

# 1. Create DataFrame
data = {
    'Name': ['Ali', 'Sara', 'John', 'Zain', 'Emma'],
    'Age': [23, 25, 22, 24, 21],
    'Marks': [85, 90, 78, 88, 95],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Karachi']
}

df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

# 2. Selecting columns
print("\nNames and Marks:")
print(df[['Name', 'Marks']])

# 3. Filtering rows
print("\nStudents with Marks > 85:")
print(df[df['Marks'] > 85])

# 4. Sorting
print("\nSorted by Age:")
print(df.sort_values(by="Age"))

# 5. Applying function
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
print("\nWith Result column:")
print(df)

# 6. Groupby
print("\nAverage Marks by City:")
print(df.groupby('City')['Marks'].mean())

# 7. Aggregation
print("\nAggregation (min, max, mean Marks by City):")
print(df.groupby('City')['Marks'].agg(['min', 'max', 'mean']))

# 8. Handling missing values
df.loc[2, 'Marks'] = np.nan  # make one value missing
print("\nAfter inserting NaN:")
print(df)

print("\nFill NaN in Marks with mean:")
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
print(df)

# 9. Pivot table
print("\nPivot Table (Marks by City):")
print(df.pivot_table(values='Marks', index='City', aggfunc='mean'))
