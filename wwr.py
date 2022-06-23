import requests
from bs4 import BeautifulSoup


baseUrl = 'https://weworkremotely.com/remote-jobs'


def get_jobs(query):
    html_doc = requests.get(f'{baseUrl}/search?term={query}').text
    print(html_doc)


get_jobs('python')
