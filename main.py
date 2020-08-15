import requests as requests
import urllib.parse
from bs4 import BeautifulSoup

print('\nMonster.com scraper\n')
base_job = input('Enter your base job: ')
specialisation = input('Enter your specialisation: ')
location = input('Enter your location: ')
print()

params = {'q': base_job, 'where': location}
encoded = urllib.parse.urlencode(params)

url = f'https://www.monster.com/jobs/search/?{encoded}'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchResults')

job_elements = results.find_all('section', class_='card-content' or 'card-content is-active')

specialised_jobs = results.find_all('h2', string=lambda text: specialisation in text.lower())

for job_element in job_elements:
    title = job_element.find('h2', class_='title')
    company = job_element.find('div', class_='company')
    location = job_element.find('div', class_='location')

    if None in (title, company, location):
        continue

    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()

for specialised_job in specialised_jobs:
    link = specialised_job.find('a')['href']
    print(specialised_job.text.strip())
    print(f'Apply here: {link}\n')

print(f'Total jobs fetched: {len(job_elements)}\nTotal specialised jobs fetched: {len(specialised_jobs)}\n')
