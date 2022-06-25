import requests
from common import *
from bs4 import BeautifulSoup


remoteok_url = 'https://remoteok.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def get_remoteok_jobs(query):
    result = []
    query = clean_str(query.strip()).replace(' ', '-')
    html_doc = requests.get(f'{remoteok_url}/remote-{query}-jobs').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup)


# get_remoteok_jobs('python')

print(requests.get(remoteok_url, headers=headers))
