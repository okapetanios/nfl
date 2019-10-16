from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import string


# Get string of uppercase alphabet
alphabet_upper = string.ascii_uppercase

BASE_URL = "https://www.pro-football-reference.com/"


html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html, "lxml")

print(soup.prettify())
for x in soup.find_all('a'):
    print(x.get_text())
