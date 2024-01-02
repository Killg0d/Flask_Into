from app import app
from flask import jsonify, request,render_template
import requests
from app import mathematics

@app.route('/search/<string:authors>')
def search(authors):
    res = requests.get("https://openlibrary.org/authors/OL23919A.json?{flask.escape(authors)}") 

    if res.status_code == 200:
        return {"message": res.json()}, 200
    elif res.status_code == 404:
        return {"message": "Something went Wrong"}, 404
    else:
        return {"message": "Server Error"}, 500


@app.route('/health', methods=["GET", "POST"])
def health_check():
    if request.method == "GET":
        return jsonify(status="OK", method="GET")

    elif request.method == "POST":
        return jsonify(status="OK", method="POST")
