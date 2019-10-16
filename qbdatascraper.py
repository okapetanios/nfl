from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import string

# Get string of uppercase alphabet
alphabet_upper = string.ascii_uppercase

BASE_URL = "https://www.pro-football-reference.com/"

# where the qb html player pages are kept. 
LOCAL_URL = "/players/qb/"


with open("nflplayers.csv", "r") as players:
    data = csv.reader(players)
    for row in data:
        
        print(row[1] == 'QB')
        # if row[1] is 'QB':
        #     name = row[0]
        #     print(name)
        #     soup = BeautifulSoup(row[2], 'lxml')

        #     f = open(LOCAL_URL + name + ".html", "w")
        #     f.write(soup.prettify())
        #     f.close()






# for i in range(len(alphabet_upper)):
#     url = BASE_URL + "players/" + alphabet_upper[i] + ".html"
#     html = urlopen(url).read()
#     soup = BeautifulSoup(html, "lxml")

#     f= open("players/players" + alphabet_upper[i] + ".html","w+")
#     f.write(soup.prettify())
#     f.close()