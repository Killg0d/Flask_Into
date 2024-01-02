from app import app
from flask import jsonify,request

@app.route('/')
def index():
    return jsonify(status="OK", method="GET")

@app.route('/health',methods=["GET","POST"])
def health_check():
    if request.method == "GET" : return jsonify(status="OK", method="GET")

    elif request.method == "POST" : return jsonify(status="OK", method="POST")
