import requests
#url = requests.get('C:\\Users\\Fitec\\PycharmProjects\\Dossier3\\venv\\test.html')
url = requests.get('https://fr.wikipedia.org/wiki/Web_scraping')

from bs4 import BeautifulSoup
soup = BeautifulSoup(url.text, 'html.parser')

results = soup.find_all('span', attrs={'class':'short-desc'})

print(len(results.read()))