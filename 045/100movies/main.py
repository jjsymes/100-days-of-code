import requests
import os
from bs4 import BeautifulSoup

directory = os.path.realpath(__file__ + f"/{os.pardir}")
output_file = f"{directory}/movies.txt"

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")

title_html_elements = soup.find_all(name="h3", class_="title")

titles = [title.get_text() for title in title_html_elements]
titles.reverse()

with open(output_file, "w") as f:
    f.write("\n".join(titles))
