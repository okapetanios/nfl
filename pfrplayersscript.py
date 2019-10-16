# This script grabs the HTML for all the players on 
# "https://www.pro-football-reference.com/" and outputs it to a subdirectory
# called players/.

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import string
import time
import random

# Get string of uppercase alphabet
alphabet_upper = string.ascii_uppercase

BASE_URL = "https://www.pro-football-reference.com/"
LOCAL_URL = "/players/"



for i in range(len(alphabet_upper)):
    url = BASE_URL + "players/" + alphabet_upper[i] + ".html"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    f= open("players/players" + alphabet_upper[i] + ".html","w+")
    f.write(soup.prettify())
    f.close()

# html = urlopen(BASE_URL).read()
# soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())
# for a in soup.find_all('a'):
#     print(a.get_text())


# div with player links
# <div class="section_content" id="div_players">

# Creates csv file
# with open('players.csv', 'w') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     filewriter.writerow(['Name', 'Profession'])
#     filewriter.writerow(['Derek', 'Software Developer'])
#     filewriter.writerow(['Steve', 'Software Developer'])
#     filewriter.writerow(['Paul', 'Manager'])