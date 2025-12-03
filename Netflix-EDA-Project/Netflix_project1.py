import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Netflix-EDA-Project/data/raw/netflix_messy.csv")

def conv_fuct(x):
    if pd.isna(x):
        return np.nan
    if "min" in x:
        return int(x.replace("min", "").strip())
    if "Season" in x:
        return int(x.replace('Seasons', "").replace("Season","").strip())
    return np.nan

 #                  Analyzing Raw Data

print(df.info())
print(df.shape)
print(df.head(20))
print(df.isnull().sum())
print(df.duplicated().sum())

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

#           Cleaning the data (Missing Values, duplicates, typos)

df['type']=df['type'].replace({'Movi':'Movie', 'TV Sho':'TV Show'})
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].replace('Not Given', 'Unknown')
df['director'] =df['director'].fillna('Unknown')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df = df.drop_duplicates()

#   Date Time format for EDA Analysis

df['date_added'] = pd.to_datetime(df['date_added'])
df['added_year'] = df['date_added'].dt.year
df['added_month'] = df['date_added'].dt.month
df['duration_clean'] = df['duration'].apply(conv_fuct)


# #       Verify Cleaned Data
print(df.columns)
print(df.head(50))
print(df.isnull().sum())
print(df.duplicated().sum())
#           Data Analyze


movies_vs_TVshow = df['type'].value_counts()
print(movies_vs_TVshow)

title_year = df['added_year'].value_counts().sort_index()
print(title_year)

top_countries = df['country'].value_counts().head(10)
print(top_countries)

common_ratings = df['rating'].value_counts()
print(common_ratings)

examle=df.describe(include='all')
print(examle)

# Content Distribution analysis

genre_list = df['listed_in'].str.split(', ')
all_genres = genre_list.explode()
genre_count = all_genres.value_counts().head(15)
print(genre_count)

#Movies VS Tv shows Analysis

movie_duration = df[df['type'] == 'Movie']['duration_clean'].describe()
print(f"Movies Duration \n {movie_duration}")

TV_show_numbers = df[df['type']=='TV Show']['duration_clean'].describe()
print(TV_show_numbers)

Tvshow_per_country = df[df['type'] == 'TV Show']['country'].value_counts().head(10)
print(f"TV Shows per country \n {Tvshow_per_country}")

Movie_production_country = df[df['type']== 'Movie']['country'].value_counts().head(10)
print(f"Movies per Country \n {Movie_production_country}")

movie_year = df[df['type']=='Movie']['added_year'].value_counts()
print(f"shows added per year \n {movie_year}")

shows_year = df[df['type'] == 'TV Show']['added_year'].value_counts()
print(f"shows added per year \n {shows_year}")

#Eploratory Data Analysis # visuallisation

print("\n--- Summary Statistics ---")
print(df.describe(include='all')) 
print("\nUnique values per column:\n", df.nunique())

sns.set(style='whitegrid')

plt.figure(figsize=(10,5))
sns.countplot(df['type'])
plt.title('Movies vs TV Show')
plt.show()

plt.figure(figsize=(12,6))
plt.bar(title_year.index, title_year.values)
plt.title("Titles Added Per Year")
plt.xlabel("Year Added")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,5))
plt.barh(top_countries.index, top_countries.values)
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Countries")
plt.show()

plt.figure(figsize=(12,5))
df['rating'].value_counts().plot(kind='barh')
plt.title("Content Rating Distribution")
plt.xlabel("Count")
plt.ylabel("Rating")
plt.show()

plt.figure(figsize=(12,6))
plt.barh(genre_count.index, genre_count.values)
plt.title("Top 15 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df[df['type'] == 'Movie']['duration_clean'], bins=30, kde=True)
plt.title("Movie Duration Distribution (Minutes)")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(12,6))
sns.countplot(data=df, x='added_year', hue='type')
plt.title("Movies vs TV Shows Added Per Year")
plt.xlabel("Year Added")
plt.ylabel("Count")
plt.legend(title="Type")
plt.xticks(rotation=90)
plt.show()