import requests
import urllib.request
import time
import bs4

url = 'http://prio.2b2t.dev/'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
soup.findAll('div')
one_a_tag = soup.findAll('div')[2]
print(one_a_tag)