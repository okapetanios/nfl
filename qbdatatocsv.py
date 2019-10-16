import csv

qb = csv.writer(open('qbcompletionwins.csv', 'w'))
qb.writerow(['Name', 'Completion%', 'Wins', 'Losses', 'Ties'])