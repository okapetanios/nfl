from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import string
import time
import random

# Get string of uppercase alphabet
alphabet_upper = string.ascii_uppercase

BASE_URL = "https://www.pro-football-reference.com/"



for i in range(len(alphabet_upper)):
    url = BASE_URL + "players/" + alphabet_upper[i] + "/"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    f= open("players/players" + alphabet_upper[i] + ".html","w+")
    f.write(soup.prettify())

# html = urlopen(BASE_URL).read()
# soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())
# for x in soup.find_all('a'):
#     print(x.get_text())
