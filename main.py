import json
import httplib2
import base64
from flask import Flask, request, make_response, redirect, url_for, jsonify
from controllers.controllers import *
from models.models import *

app = Flask(__name__)
student = Student()


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "" or password == "":
        return jsonify("Fuck You")
    else:
        global student
        student = login_and_fetch_details(username, password)
        if student is None:
            return "Wrong Details"
    return jsonify(student.toJSON())


@app.route('/att', methods=['GET'])
def get_attendance():
    attendance = fetch_attendance(student)
    return jsonify(attendance)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
