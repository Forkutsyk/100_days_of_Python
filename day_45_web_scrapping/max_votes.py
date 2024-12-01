from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')


titles = soup.find_all(name="span", class_="titleline")
score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

article_texts = []
article_links = []

for article_tag in titles:
    text = article_tag.a.getText()
    article_texts.append(text)
    link = article_tag.a.get('href')
    article_links.append(link)
biggest_score = max(score)
biggest_score_index = score.index(biggest_score)+1

print(article_texts[biggest_score_index])
print(article_links[biggest_score_index])
print(biggest_score)
