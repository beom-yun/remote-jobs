import requests
from common import *
from bs4 import BeautifulSoup


wwr_url = 'https://weworkremotely.com'


def get_wwr_jobs(query):
    result = []
    query = clean_str(query.strip()).replace(' ', '+')
    html_doc = requests.get(f'{wwr_url}/remote-jobs/search?term={query}').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    jobs = soup.find_all('li', {'class': 'feature'})
    for job in jobs:
        company = clean_str(job.find('span', {'class': 'company'}).string)
        title = clean_str(job.find('span', {'class': 'title'}).string)
        link = wwr_url + clean_str(job.find_all('a')[1].get('href'))
        result.append({
            'company': company,
            'title': title,
            'link': link
        })
    return result


js = get_wwr_jobs('python')
print('wwr', len(js), 'jobs')
for j in js:
    print(j)
