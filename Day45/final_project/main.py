# top 100 movies
import requests
import bs4

URL = "https://stacker.com/stories/1587/100-best-movies-all-time"

response = requests.get(url=URL)
movies_text = response.text
soup = bs4.BeautifulSoup(movies_text, "html.parser")
all_movies = soup.find_all(name="h2", class_="ct-slideshow__slide__text-container__caption")
movies_title = [movies.getText() for movies in all_movies]

converted_movies = []
for mero_movie in movies_title:
    converted_movies.append(mero_movie.strip())

movie_title_main = converted_movies[0]  # 100 best movies of all time
another_converted_movies = converted_movies
another_converted_movies.remove("100 best movies of all time")
my_movie_list = another_converted_movies[::-1]  # list of movies

with open("My Movies List", mode="w") as data:
    data.write(movie_title_main)
    data.write("\n")
    data.write("___________________________")
    data.write("\n")
    for my_data in my_movie_list:
        data.write(f"{my_data}\n")