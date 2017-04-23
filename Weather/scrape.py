from twython import Twython
import csv

CONSUMER_KEY = 'abjfNXUtEsKvKCvbs4koJ4sx7'
CONSUMER_SECRET = '5wzIQqg1kYdPKYYxHHvxfymuCKYMphfdZ7G92j240cjF4aeEMD'
ACCESS_TOKEN = '852283264463245312-K6W8DXylWeMrCSEf7iDGRrDClp2eR9C'
ACCESS_TOKEN_SECRET = 'qmq9uluDLxWUlDGwyuMoRhR9FnLpPwev3dk7pc4mdYDA0'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

import requests
url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Washington, DC'}
r = requests.get(url, params=params)
results = r.json()['results']
location = results[0]['geometry']['location']
location['lat'], location['lng']
(38.883723, 77.038866)

import csv
import requests
from BeautifulSoup import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://weather.com/weather/hourbyhour/l/26636:21:US'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("tidal_basin_weather.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["time", "descriptions", "temp", "feels", "precip", "humidity", "wind"])
writer.writerows(list_of_rows)

search = twitter.search(q='Cherry Blossoms', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Cherry Blossoms', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['Cherry Blossoms', result['text'].encode('utf-8'), url]]
        a.writerows((text))

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e

# read from csv