import requests
from bs4 import BeautifulSoup

response = requests.get("https://stacker.com/stories/1587/100-best-movies-all-time")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
movie_titles = [movie.getText() for movie in soup.select(".ct-slideshow__slide__text-container__caption div")]
movie_titles.remove(movie_titles[0])
movie_titles.reverse()
new_movie_titles = [movie[1:] for movie in movie_titles]

with open("Must To See.txt", 'w') as file:
    for movie in new_movie_titles:
        file.write(f"{movie}\n")
