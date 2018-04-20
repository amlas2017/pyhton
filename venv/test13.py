import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

results = soup.find_all(id = "first")
print(results)

#print(soup.select("div p"))

#records = []
#for result in results:

