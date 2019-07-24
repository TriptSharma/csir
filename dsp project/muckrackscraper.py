import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_excel('DSv4.1.xlsx')

for name in df['Reporter Name']:
	try:
		first, last = name.split(' ')

		url = 'https://muckrack.com/{}-{}'.format(first, last)
		# headers = {	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')

		twitter = soup.find_all('div', attrs={'class':'col-xs-6 js-icon-twitter'})
		if twitter is not None:
			twitter_link = twitter.find('a', href=True)
			print(twitter_link)
		else:
			print('Not found')
	except:
		print("long name; not found")