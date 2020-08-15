import requests as requests
import urllib.parse
from bs4 import BeautifulSoup

print('\nFlipkart scraper\n')
search_term = input('Enter your search term: ')
print()

params = {'q': search_term}
encoded = urllib.parse.urlencode(params)

url = f'https://www.flipkart.com/search?{encoded}'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div', class_='_1HmYoV _35HD7C')

print(results)
