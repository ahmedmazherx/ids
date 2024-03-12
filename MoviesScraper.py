import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.imdb.com/chart/top/'
# As the server refuses to authorize the request, a user header is created
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f"Error: {response.status_code}")

containers = soup.find_all('li', class_='ipc-metadata-list-summary-item')

# Lists to store Movie Title, Stars, and Ratings, Release Year
movie_title = []
movie_ratings = []
release_year = []
movie_duration = []

# Extract Movie information
for container in containers:
    # Extracting movie title
    title = container.find('h3', class_='ipc-title__text').text.strip().split('.')[1]
    movie_title.append(title)

    # Extracting movie stars
    stars = container.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.strip()[0:4]
    movie_ratings.append(stars)

    # Extracting movie release year
    year = container.find('span', class_='sc-b0691f29-8 ilsLEX cli-title-metadata-item').text
    release_year.append(year)

    # Extracting movie duration
    duration = container.find_all('span', class_='sc-b0691f29-8 ilsLEX cli-title-metadata-item')[1].text
    movie_duration.append(duration)

data = {"movie_title": movie_title,
        "movie_ratings": movie_ratings,
        "release_year": release_year,
        "movie_duration": movie_duration}

filename = "imdb_top_movies.csv"

# Writing data to CSV
with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:  # Change encoding to 'utf-8-sig'
    fieldnames = ['movie_title', 'movie_ratings', 'release_year', 'movie_duration']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write rows
    for i in range(len(movie_title)):
        writer.writerow({'movie_title': movie_title[i],
                         'release_year': release_year[i],
                         'movie_duration': movie_duration[i],
                         'movie_ratings': movie_ratings[i]})
print(f"Data saved to {filename} successfully!")
