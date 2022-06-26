from common import clean_str
from flask import Flask, redirect, render_template, request
from scrap import get_all_jobs

app = Flask("SuperScrapper")
fake_db = dict()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/report')
def report():
    word = clean_str(request.args.get('word').lower())
    if not word:
        return redirect('/')
    if word in fake_db:
        jobs = fake_db[word]
    else:
        jobs = get_all_jobs(word)
        fake_db[word] = jobs
    print(jobs)

    return render_template(
        "report.html",
        searching_by=word,
        len_indeed=str(len(jobs['indeed'])),
        len_remoteok=str(len(jobs['remoteok'])),
        len_wwr=str(len(jobs['wwr'])),
        jobs=jobs
    )


app.run()
