from date import Date
import bs4
import requests

URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

mero_date = Date()
response = requests.get(URL)
mero_soup = response.text
soup = bs4.BeautifulSoup(mero_soup, "html.parser")
