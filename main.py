from common import clean_str
from flask import Flask, redirect, render_template, request
from scrap import get_all_jobs

app = Flask("SuperScrapper")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/report')
def report():
    word = clean_str(request.args.get('word').lower())
    if not word:
        return redirect('/')
    jobs = get_all_jobs(word)
    print(len(jobs))
    return render_template("report.html", searching_by=word)


app.run()
