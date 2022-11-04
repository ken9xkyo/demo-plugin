from flask import Flask, render_template, make_response
import requests
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
# ok
# CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/plugin-vod-token")
@cross_origin(supports_credentials=True,methods="get")
def token():
    url = "https://vodbizflyapi.cnnd.vn/oauth/token"
    payload = {'username': "quangnn_bizflyvod-quangnnvod-141e7",
               'grant_type': 'authorization_code',
               'code': '4dmilvwp3u',
               'scope': '497318801742135296'}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = requests.post(url, headers=headers, data=payload)
    response = make_response(data.json()["message"]["token"], 200)

    return response


@app.route("/")
def home():
    return render_template("cms.html")

