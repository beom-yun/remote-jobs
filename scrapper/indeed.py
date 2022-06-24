import requests
from common import *
from bs4 import BeautifulSoup


indeed_url = 'https://www.indeed.com'


def get_indeed_jobs(query):
    result = []
    query = clean_str(query.strip()).replace(' ', '+')
    html_doc = requests.get(
        f'{indeed_url}/jobs?q=remote+{query}&limit=50').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    jobs = soup.find_all('td', {'class': 'resultContent'})
    for job in jobs:
        company = clean_str(job.find('span', {'class': 'companyName'}).string)
        job = job.find('a', {'class': 'jcs-JobTitle'})
        title = clean_str(job.find('span').string)
        link = indeed_url + clean_str(job.get('href'))
        result.append({
            'company': company,
            'title': title,
            'link': link
        })
    return result


js = get_indeed_jobs('python')
print('indeed', len(js), 'jobs')
for j in js:
    print(j)
