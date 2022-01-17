import bs4
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = bs4.BeautifulSoup(response.text, "html.parser")
song_title = soup.find_all("li", class_="o-chart-results-list__item")
songs = [song.getText() for song in song_title]
print(songs)

# from bs4 import BeautifulSoup
# import requests
#
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.find_all("span", class_="chart-element__information__song")
# song_names = [song.getText() for song in song_names_spans]
# print(song_names)
