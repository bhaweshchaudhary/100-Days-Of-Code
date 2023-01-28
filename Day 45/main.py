from bs4 import BeautifulSoup
import requests
import prettify

response = requests.get(url="https://news.ycombinator.com/news")
response.ok
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
articles_text = []
articles_link = []
for article_tag in articles:
    article_text = article_tag.getText()
    articles_text.append(article_text)
    article_link = article_tag.get("href")
    articles_link.append(article_link)
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(articles_text, articles_link, article_upvote, sep="\n")
largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(articles_text[largest_index], articles_link[largest_index], sep="\n")