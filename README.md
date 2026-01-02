## Objectives
- Understand the structure and quality of the raw dataset
- Clean missing values, duplicates, and typos
- Standardize date and duration fields
- Analyze:
  - Movies vs TV Shows distribution
  - Content added over time
  - Top content-producing countries
  - Ratings distribution
  - Genre popularity
  - Duration patterns for movies and TV shows
- Visualize insights using charts and plots


## Data Cleaning
The following steps were performed:
- Fixed typos in the `type` column (e.g., *Movi* → *Movie*, *TV Sho* → *TV Show*)
- Filled missing values in categorical columns (`country`, `director`)
- Converted `date_added` to datetime format
- Removed duplicate records
- Extracted new features:
  - `added_year`
  - `added_month`
- Cleaned `duration`:
  - Movies → duration in minutes
  - TV Shows → number of seasons

## Analysis Performed
- **Content Distribution**: Movies vs TV Shows
- **Time-Based Analysis**: Titles added per year
- **Country Analysis**: Top 10 content-producing countries
- **Ratings Analysis**: Frequency of maturity ratings
- **Genre Analysis**: Top 15 genres on Netflix
- **Duration Analysis**:
  - Distribution of movie runtimes
  - Season count distribution for TV shows

## Visualizations
The project includes:
- Count plots (Movies vs TV Shows)
- Bar charts (Titles added per year)
- Horizontal bar charts (Top countries, genres, ratings)
- Histogram of movie durations
- Year-wise comparison of Movies vs TV Shows

Visualizations are created using **Matplotlib** and **Seaborn**.


## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
