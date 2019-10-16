# This script constructs a playerinfo.csv out of the alphabetical player html
# pages in subdirectory players/.

from bs4 import BeautifulSoup
import csv
import string
import time
import re

# Get string of uppercase alphabet
alphabet_upper = string.ascii_uppercase

LOCAL_FILE = "players/"
POSITION_SET = set()
# Creates csv file
playerscsv = csv.writer(open('nflplayers.csv', 'w'))
playerscsv.writerow(['Name', 'Position', 'PFRLink', 'Active'])

for i in range(len(alphabet_upper)):
    f = open(LOCAL_FILE + "players" + alphabet_upper[i] + ".html","r")
    soup = BeautifulSoup(f, "lxml")
    section = soup.find(id='div_players')
    player_info = section.find_all('p')
    for player in player_info:
        link = "pro-football-reference.com/" + player.a["href"]
        name = player.a.get_text().strip()
        
        try:
            position = re.search(r"\(([^)]+)\)", player.get_text()).group()
            position = position.strip('()')
        except:
            position = "Unassigned"
        
        POSITION_SET.add(position)

        if(player.b):
            active = "yes"
        else:
            active = "no"
        playerscsv.writerow([name, position, link, active])  
    f.close()

# html = urlopen(BASE_URL).read()
# soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())
# for a in soup.find_all('a'):
#     print(a.get_text())


# div with player links
# <div class="section_content" id="div_players">

