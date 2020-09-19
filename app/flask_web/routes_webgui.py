import datetime
from datetime import timedelta
from flask import Flask, render_template, session, redirect, flash, request
import logging
import json
from app.flask_web import app
from app.sales import Sales

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:\t%(message)s')


@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)


@app.route("/", methods=["GET"])
def home():
    #form = HomeForm()

    d = datetime.date.today()
    s = Sales(d)

    today = f'Today is {d.strftime("%A %d of %B, %Y")}'

    if s.is_second_sunday_of_month():
        message = "TODAY is the Second Sunday of the Month!!!"
    else:
        message = f"It is <b>NOT</b> the Second Sunday of the Month... "
        message += f'The next Second Sunday is <em>{s.next_second_sunday().strftime("%A %d of %B, %Y")}</em> '
        delta = s.next_second_sunday() - d
        message += f"in <b>{delta.days} days</b> from now"

    return render_template('home.html', title="Home", today=today, message=message), 200
