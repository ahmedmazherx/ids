# 28-march-2024
# CSC461 – Assignment2 – IDS – Data Visualization
# Ahmed Mazher
# FA20-BSE046
# The world population dataset from 1960 to 2020 allows for the creation of charts to compare the populations of the top 10 most populous countries, display the populations of the 10 least populous countries in 2015, and visualize the population changes of Pakistan, India, the United States, and the United Kingdom from 1970 to 2010, as well as Pakistan's population growth between 2010 and 2020.



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('./sample_data/world_pop.csv')

# Melt the DataFrame to convert it from wide format to long format
df_melted = df.melt(id_vars=['country'], var_name='Year', value_name='Population')
df_melted['Year'] = df_melted['Year'].str.replace('year_', '').astype(int)  # Convert 'Year' to integer.

# Filter to get the top 10 countries based on population in 2020
top_10_countries_2020 = df_melted[df_melted['Year'] == 2020].nlargest(10, 'Population')['country']

# Filter the melted DataFrame to only include data for the top 10 countries
df_top_10 = df_melted[df_melted['country'].isin(top_10_countries_2020)]

# Plotting the population growth of the top 10 most populated countries (1960-2020)
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_top_10, x='Year', y='Population', hue='country', marker='o', palette='tab10')
plt.title('Population Growth of the Top 10 Most Populated Countries (1960-2020)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# For showing the population of the 10 least populous countries in 2015:
least_populous_2015 = df.nsmallest(10, 'year_2015')[['country', 'year_2015']].set_index('country')
least_populous_2015.plot(kind='bar', legend=None)
plt.title('10 Least Populous Countries in 2015')
plt.xlabel('Country')
plt.ylabel('Population')
plt.tight_layout()
plt.show()

# For calculating and showing the population change from 1970 to 2010:
df['population_change_1970_to_2010'] = (df['year_2010'] - df['year_1970']) / 1e6  # Convert to millions
selected_countries_change = df[df['country'].isin(['Pakistan', 'India', 'United States', 'United Kingdom'])]
sns.barplot(data=selected_countries_change, x='country', y='population_change_1970_to_2010')
plt.title('Population Change from 1970 to 2010 (in millions)')
plt.ylabel('Population Change (in millions)')
plt.xlabel('Country')
plt.tight_layout()
plt.show()

# For calculating and showing Pakistan's population growth from 2010 to 2020:
pakistan_growth = (df[df['country'] == 'Pakistan']['year_2020'] - df[df['country'] == 'Pakistan']['year_2010']) / 1e6
pakistan_growth.plot(kind='bar')
plt.title('Pakistan Population Growth from 2010 to 2020 (in millions)')
plt.ylabel('Population Growth (in millions)')
plt.xlabel('Year')
plt.xticks([])
plt.tight_layout()
plt.show()
