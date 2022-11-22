from flask import Flask, render_template, make_response
import requests
from flask_cors import cross_origin

app = Flask(__name__)

# Api lấy token cho plugin
@app.route("/plugin-vod-token")
@cross_origin(supports_credentials=True,methods="get")
def token():
    # Khởi tạo tham số
    username = "" # Nhập username
    account_suffix = "" # Nhập Account Suffix
    code = "" # Nhập code
    scope = "" # Nhập scope
    url = # Nhập url

    # Tạo payload
    payload = {'username': f"{username}{account_suffix}",
               'grant_type': 'authorization_code',
               'code': code,
               'scope': scope}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Gọi request lấy token
    data = requests.post(url, headers=headers, data=payload)

    # Xử lý response
    """
    Dữ liệu response trả về có dạng:
    {
        "message":{
            "token":"epBJqhqG1f7ObEks670-4NUX9X4QemxldFR3Hw...",
            "expires":"2m"
        },
        "status":1
    }
    Cần lấy trường token và trả ra
    """
    token = data.json()["message"]["token"]
    response = make_response(token, 200)

    return response

# Demo CMS.html
@app.route("/")
def home():
    return render_template("cms.html")

