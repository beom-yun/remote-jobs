from common import clean_str, save_to_file
from flask import Flask, redirect, render_template, request, send_file
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


@app.route('/export')
def export():
    try:
        word = clean_str(request.args.get('word').lower())
        print('word', word)
        if not word:
            raise Exception()
        jobs = []
        for values in fake_db[word].values():
            jobs += values
        print('jobs', jobs)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file('jobs.csv', download_name='SearchingResult.csv', as_attachment=True)
    except:
        return redirect('/')


app.run()
