from scrapper.indeed import *
from scrapper.remoteok import *
from scrapper.wwr import *


def get_all_jobs(word):
    return {
        'indeed': get_indeed_jobs(word),
        'remoteok': get_remoteok_jobs(word),
        'wwr': get_wwr_jobs(word)
    }
