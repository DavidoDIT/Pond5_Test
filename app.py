from flask import Flask, jsonify
from bs4 import BeautifulSoup
import platform
import requests


app = Flask(__name__)

page = requests.get("https://www.pond5.com/photo/11497188/")
print(page.status_code)  # Checking for a 200 response

pic_soup = BeautifulSoup(page.text, 'html.parser')
type(pic_soup)


@app.route('/')
def test():
    test = "Test"
    return test

@app.route('/ping')
def ping():
    if page.status_code == 200:
        return "PONG!"
    else:
        return "Error"

@app.route('/system')
def system():
    info = {"version": platform.uname().version,
            "system": platform.uname().system,
            "processor": platform.processor(),
            "architecture": platform.architecture()}
    return jsonify(info)


@app.route('/mediainfo')
def pic():
    return pic

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)





