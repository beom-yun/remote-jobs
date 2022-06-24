import requests
from common import *
from bs4 import BeautifulSoup


remoteok_url = 'https://remoteok.com'


def get_remoteok_jobs(query):
    result = []
    query = clean_str(query.strip()).replace(' ', '-')
    html_doc = requests.get(f'{remoteok_url}/remote-{query}-jobs').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup)


# get_remoteok_jobs('python')
print(requests.get(f'{remoteok_url}'))
