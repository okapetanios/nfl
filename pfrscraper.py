from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

BASE_URL = "https://www.pro-football-reference.com/"


# def get_category_links(section_url):
#     html = urlopen(section_url).read()
#     soup = BeautifulSoup(html, "lxml")
#     years = soup.find("li", id="header_years")
#     category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
#     return category_links

html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html, "lxml")
for x in soup.find_all('a'):
    print(x.get_text())
