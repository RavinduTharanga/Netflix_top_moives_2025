from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

import csv

# Downloading imdb top 250 movie's data
url = 'https://www.netflix.com/tudum/top10'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")



movies = soup.select('td button')

view = soup.find_all('td', class_='views')

movie_names = []
for movie in movies:
    movie_names.append(movie.text)

views = []

for div in view:
    text = div.get_text()
    views.append(text.replace(",",""))  


res = dict(zip(movie_names, views))

# for x, y in res.items():
#   print("movie name:",x, "views:",y)

# field_names = ['movie', 'views'] 


csv_file = 'netflix.csv'

# Writing to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Movie Name', 'Views'])
	
    # Write data
    for key, value in res.items():
        writer.writerow([key, value])

print(f"Dictionary saved to {csv_file}")

# print(res)