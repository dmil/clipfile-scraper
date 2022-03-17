import requests
from bs4 import BeautifulSoup
import pandas as pd


articles = []

for page in range(1,7):

	# search for "TAKS" and "cheating"
	url = f"http://clipfile.org/?paged={page}&s=taks+cheating"

	print(f"Scraping {url}")
	response = requests.get(url, headers={"User-Agent": "XY"})
	soup = BeautifulSoup(response.content, 'html.parser')
	for article in soup.find_all('article'):
		articles.append({
			'headline': article.find('header').text.strip(),
			'time': article.find('time').text.strip(),
			'datetime': article.find('time')['datetime'],
			'url': article.find('header').find('a')['href']
			})

df = pd.DataFrame(articles)
df.sort_values(by='datetime', ascending=True)\
	.to_csv('df.csv', index=False)