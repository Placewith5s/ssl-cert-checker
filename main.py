import requests
import certifi
from flask import Flask, render_template
from flask import request

app: Flask = Flask(__name__)

@app.route("/")
def home() -> str:
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e) -> str:
    return render_template("404.html")
@app.errorhandler(500)
def internal_error(e) -> str:
    return render_template("500.html")

def handle_self_url(url: str) -> None:
    if url == "https://cert-checker-1gbs.onrender.com/":
        url = ""
        app.logger.error("Cannot check self!")

@app.route("/check", methods=["POST"])
def main() -> str:
    url: str = request.form.get("url")

    handle_self_url(url)

    try:
        proxies: dict[str, str] = {
            "http": "",
            "https": ""
        }

        requests.get(url, verify=certifi.where(), proxies=proxies)
        return render_template("result.html", result="SSL verification successful ✅!", url=url)
    except requests.exceptions.SSLError as err:
        app.logger.warning(f"SSL verification failed! {err}")
        return render_template("result.html", result="SSL verification failed ❌!", url=url)
    except Exception as err:
        app.logger.error(f"Something went wrong! {err}")
        return render_template("result.html", result="Something went wrong! ⚠️", url=url)

if __name__ == '__main__':
    app.run()