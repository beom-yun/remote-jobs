from scrapper.indeed import *
from scrapper.remoteok import *
from scrapper.wwr import *


def get_all_jobs(word):
    indeed_jobs = get_indeed_jobs(word)
    remoteok_jobs = get_remoteok_jobs(word)
    wwr_jobs = get_wwr_jobs(word)
    return indeed_jobs + remoteok_jobs + wwr_jobs
