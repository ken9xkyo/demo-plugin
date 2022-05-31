from flask import Flask
import requests

app = Flask(__name__)

@app.route("/plugin-vod-token")
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
    response = data.json()["message"]["token"]
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route("/")
def home_view():
	return "<h1>Welcome to Geeks for Geeks</h1>"

