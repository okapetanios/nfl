# This script grabs the HTML for all the players on 
# "https://www.pro-football-reference.com/" and outputs it to a subdirectory
# called players/.

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import string


# Get string of uppercase alphabet
alphabet_upper = string.ascii_uppercase

BASE_URL = "https://www.pro-football-reference.com/"
LOCAL_URL = "/players/"



for i in range(len(alphabet_upper)):
    url = BASE_URL + "players/" + alphabet_upper[i] + "/"
    
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    f= open("players/players" + alphabet_upper[i] + ".html","w+")
    f.write(soup.prettify())
    f.close()
