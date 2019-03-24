from flask import Flask, jsonify
from bs4 import BeautifulSoup
import platform
import requests

app = Flask(__name__)


@app.route("/")
def test():
    test = "Test"
    return test


@app.route("/ping", methods=["GET"])
def ping():
    pond = requests.get("https://www.pond5.com/photo/11497188")
    if pond.status_code == 200:
        return "PONG!"
    else:
        return "Error"


@app.route("/system")
def system():
    info = {
        "version": platform.uname().version,
        "system": platform.uname().system,
        "processor": platform.processor(),
        "architecture": platform.architecture(),
    }
    return jsonify(info)


@app.route("/mediainfo/<media_id>", methods=["GET"])
def media(media_id):
    page = requests.get("https://www.pond5.com/photo/" + str(media_id))
    print(page.status_code)  # Checking for a 200 response
    soup = BeautifulSoup(page.text, "html.parser")
    filename = soup.find("meta", property="og:image")
    filename = filename["content"]
    height = soup.find("meta", property="og:image:height")
    height = height["content"]
    width = soup.find("meta", property="og:image:width")
    width = width["content"]
    title = soup.find("meta", property="twitter:title")
    title = title["content"]
    size = soup.find_all("dd")[12].text

    pic_info = {
        "filename": filename,
        "size": size,
        "height": height,
        "width": width,
        "title": title,
    }

    return jsonify(pic_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
