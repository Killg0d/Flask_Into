import datetime
from flask import Flask,render_template

app = Flask("Maths problem solver")

app.config.from_object("config.DevelopmentConfig")


@app.route('/')
def index():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


from app import views


