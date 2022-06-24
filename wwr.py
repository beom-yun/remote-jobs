import requests
from common import *
from bs4 import BeautifulSoup


baseUrl = 'https://weworkremotely.com'


def get_jobs(query):
    result = []
    html_doc = requests.get(f'{baseUrl}/remote-jobs/search?term={query}').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    jobs = soup.find_all('li', {'class': 'feature'})
    for job in jobs:
        company = clean_str(job.find('span', {'class': 'company'}).string)
        title = clean_str(job.find('span', {'class': 'title'}).string)
        location = clean_str(
            job.find('span', {'class': 'region company'}).string)
        link = clean_str(baseUrl + job.find_all('a')[1].get('href'))
        result.append(','.join([company, title, location, link]))
    return result


for j in get_jobs('python'):
    print(j)
# print(clean_str('   sd s d     d   '))
