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

for row in list_of_rows:
    if 'am' in row[1]:
        flag = 'am'
    else:
        flag = 'pm'
    time, day = row[1].split(flag)
    dt = datetime.strptime(str(datetime.today().month) + ' ' + str(datetime.today().day) + ' ' + str(datetime.today().year) + ' ' + time.strip() + flag.upper(), "%m %d %Y %I:%M%p")
    row.append(dt)

search = twitter.search(q='Tidal Basin', count="100")
tweets = search['statuses']

for tweet in tweets:
    # convert timestamp to a DateTime object
    # ts = datetime.strptime()
    # get the hour of the tweet (maybe the minute)
    # ts.hour
    # in list_of_rows, find the reading that corresponds to that hour and day
    match = next(row for row in list_of_rows if row[8].hour == ts.hour and row[8].day == ts.day)
    if match:
        tweet.update_status("It was %s with %s when %s posted at %s: %s" % (match[3], match[2], tweet['screen_name'], match['time'], tweet['entities']['urls'][0]['expanded_url'])
    else:
        # we couldn't find a weather reading for this tweet


with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Tidal Basin', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['Tidal Basin', result['text'].encode('utf-8'), url]]
        a.writerows((text))