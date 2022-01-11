import os
from bs4 import BeautifulSoup
import requests

directory = os.path.realpath(__file__ + f"/{os.pardir}")
website_file = f"{directory}/website.html"

with open(website_file) as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print(soup.find(class_="heading"))

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

links = soup.select(".titlelink")
votes = soup.find_all(name="span", class_="score")

articles = []

for index, link in enumerate(links):
    votes_element = link.find_parent(class_="athing").next_sibling()[1].find(name="span", class_="score")
    if votes_element:
        votes = int(votes_element.get_text().split()[0])
    else:
        votes = None

    if votes:
        articles.append({
            "link": link.get("href"),
            "title": link.get_text(),
            "votes": votes
        })

max_voted_article = max(articles, key=lambda article: article['votes'])
print(f"Max voted article:\ntitle={max_voted_article['title']}\nlink={max_voted_article['link']}\nvotes={max_voted_article['votes']}")