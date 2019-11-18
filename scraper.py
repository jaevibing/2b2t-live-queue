import requests
import urllib.request
import time
import bs4

url = 'http://prio.2b2t.dev/'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
soup.findAll('div')
prioq = soup.findAll('div')[2]

url = 'http://2b2t.io/'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
soup.findAll('h1')
queue = soup.findAll('h1')

print('2b2t normal queue is '+ queue + '. 2b2t priority queue is ' + prioq + '.')
