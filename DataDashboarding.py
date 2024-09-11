import requests
import json
import pandas as pd
import plotly.express as px

# Reading your personal API Key from 'secrets.txt' (mine is a .gitignore)
with open('secrets.txt', 'r') as file:
    api_key = file.readline().strip()

# Loading a mock JSON to demonstrate the project without an API key
file_path = "example.json"
with open(file_path, 'r') as file:
    mock_data = json.load(file)
chosen_movie_data = mock_data

# todo Uncomment the lines below to use the API instead of mock data
'''
url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
response = requests.get(url)
if response.status_code == 200:
    live_data = response.json()['results']
else:
    print('Failed to fetch data')
    live_data = []
chosen_movie_data = live_data
'''

movie_list = []

for movie in chosen_movie_data:
    movie_info = {
        'title': movie['title'],
        'vote_average': movie['vote_average'],
    }
    movie_list.append(movie_info)

titles = []
vote_averages = []

for movie in movie_list:
    title = movie['title']
    titles.append(title)
    vote_average = movie['vote_average']
    vote_averages.append(vote_average)

movie_df = pd.DataFrame(movie_list)
sorted_movie_df = movie_df.sort_values(by='vote_average', ascending=False)

fig = px.bar(
    data_frame=sorted_movie_df,
    x='title',
    y='vote_average',
    labels={'title': 'Movie Title', 'vote_average': 'Vote Average'},
    title='Movies Ordered by Vote Averages'
)

fig.show()
