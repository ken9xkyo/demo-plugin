from flask import Flask, render_template, make_response
import requests
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
# ok
# CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/plugin-vod-token")
@cross_origin()
def token():
    url = "https://h41.cnnd.vn/digital-vod/oauth/token"
    payload = {'username': "quangnn_bizflyvod-staging-khodemo-e6bd1",
               'grant_type': 'authorization_code',
               'code': 'g3879u4ypf',
               'scope': '442963536461799424'}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = requests.post(url, headers=headers, data=payload)
    response = make_response(data.json()["message"]["token"], 200)

    return response


@app.route("/")
def home():
    return render_template("cms.html")

