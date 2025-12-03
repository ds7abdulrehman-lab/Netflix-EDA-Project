import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/raw/netflix_messy.csv")

def conv_fuct(x):
    if pd.isna(x):
        return np.nan
    if "min" in x:
        return int(x.replace("min", "").strip())
    if "Season" in x:
        return int(x.replace('Seasons', "").replace("Season","").strip())
    return np.nan

 #                  Analyzing
# print(df.info())
# print(df.shape)
# print(df.head(20))
# print(df.isnull().sum())
# print(df.duplicated().sum())

cat_col = ['type', 'country', 'director', 'rating', 'listed_in']
numeric_cols = ['release_year']
date_cols = ['date_added']

for col in cat_col:
    print(f'coulumn: {col}')
    print(df[col].value_counts(dropna=False))

for col in numeric_cols:
    print(f'Coulumn: {col}')
    print(df[col].describe())

for col in date_cols:
    print(f'CoulumnL: {col}')
    print(df[col].unique()[:50])


#           cleaning the data


df['type']=df['type'].replace({'Movi':'Movie', 'TV Sho':'TV Show'})
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].replace('Not Given', 'Unknown')
df['director'] =df['director'].fillna('Unknown')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df = df.drop_duplicates()
# df['date_added'] = pd.to_datetime(df['date_added'])
df['added_year'] = df['date_added'].dt.year
df['added_month'] = df['date_added'].dt.month
df['duration_clean'] = df['duration'].apply(conv_fuct)


#       Verify cleaned data
print(df.columns)
print(df.head(50))

# Data Analyze

movies_vs_TVshow = df['type'].value_counts()
print(movies_vs_TVshow)
title_year = df['added_year'].value_counts().sort_index()
print(title_year)
top_cities = df['country'].value_counts().head(10)
print(top_cities)
common_ratings = df['rating'].value_counts()
print(common_ratings)
examle=df.describe(include='all')
print(examle)

genre_list = df['listed_in'].str.split(', ')
all_genres = genre_list.explode()
genre_count = all_genres.value_counts().head(15)
print(genre_count)

movie_duration = df[df['type'] == 'Movie']['duration_clean'].describe()
print(movie_duration)
tv_shows = df[df['type'] == 'Movie']['country'].value_counts().head(10)

print(tv_shows)
