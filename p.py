import csv
from bs4 import BeautifulSoup as bs
import requests
cafes = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
def filter(s):
    for p in range(len(s)):
        if s[p].find("London Underground") != -1 or s[p].find("London Overground") != -1 or s[p].find("Docklands Light Railway") != -1 or  s[p].find("National Rail") != -1 or s[p].find("River Bus") != -1 or s[p].find("Elizabeth line" != -1):
            return True
    return False
def replace(s, zone):
    s[3] = "Zone " + str(zone+1)
    s.pop(1)
    return z
urls = ["https://en.wikipedia.org/wiki/List_of_stations_in_London_fare_zone_2"]
for q in range(len(urls)):
    s = bs(requests.get(urls[q], headers=headers).text, 'lxml')
    match = s.find_all('tr');
    for i in range(len(match)):
        m = match[i].text.split('\n')
        z = []
        for n in range(len(m)):
            if n%2 == 0 or n == 0:
                continue
            z.append(m[n])
        if filter(z): #optional
            z = replace(z, q+1) #optional
            cafes.append(z)
for i in range(len(cafes)):
    print(cafes[i])


data = [
    ['Name','Type','Zone']
]
read_file_path = 'Original.csv'
with open(read_file_path, 'r') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        r = row
        data.append(r)
file_path = 'Train.csv'
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    writer.writerows(cafes)
print('Data written to the CSV file successfully.')

