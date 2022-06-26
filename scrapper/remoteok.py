import requests
from common import *
from bs4 import BeautifulSoup


remoteok_url = 'https://remoteok.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def get_remoteok_jobs(query):
    result = []
    query = clean_str(query.strip()).replace(' ', '-')
    html_doc = requests.get(
        f'{remoteok_url}/remote-{query}-jobs?hide_closed=true', headers=headers).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    jobs = soup.find_all('td', {'class': 'company_and_position'})
    for job in jobs:
        try:
            company = clean_str(job.find('h3', {'itemprop': 'name'}).string)
            title = clean_str(job.find('h2', {'itemprop': 'title'}).string)
            link = remoteok_url + \
                clean_str(job.find('a', {'class': 'preventLink'}).get('href'))
            result.append({
                'company': company,
                'title': title,
                'link': link
            })
        except:
            continue
    return result


js = get_remoteok_jobs('python')
print('remoteok', len(js), 'jobs')
for j in js:
    print(j)
