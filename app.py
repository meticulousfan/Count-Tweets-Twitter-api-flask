from flask import Flask, render_template, request, redirect, session, url_for
import config
import stock
from flask_wtf import FlaskForm
from wtforms import Form, SelectField, SubmitField
from flask_session import Session
import json
import tweepy

app = config.configapp(Flask(__name__))
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():

    bearer_token = app.config["TOKEN"]
    headers = stock.create_headers(bearer_token)
    keyword = "xbox lang:en"
    start_time = "2021-03-01T00:00:00.000Z"
    end_time = "2021-03-31T00:00:00.000Z"
    max_results = 15
    url = stock.create_url(keyword, start_time,end_time, max_results)
    json_response = stock.connect_to_endpoint(url[0], headers, url[1])
    print(json.dumps(json_response, indent=4, sort_keys=True))
    return render_template("base.html")

if __name__ == '__main__':
   app.run(debug = True, port=6003)