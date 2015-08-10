import requests
import bs4

def get_links():
    response = requests.get('http://uhrforum.de/angebote/')
    soup = bs4.BeautifulSoup(response.text, "lxml")
    return[h3.get('href') for h3 in soup.select('h3.threadtitle a[href]')]

print(get_links())

