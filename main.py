# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
from flask_restful import Api, Resource
from flask import request
from config import app, db
import LocateShareAPI
import UserManagerAPI
from flask import url_for
import os


@app.route('/search', methods=['GET'])
def search():
    j = request.get_json(force=True)
    userId = j['userId']
    currentCity = j['currentCity']
    return LocateShareAPI.search_api(userId, currentCity)


@app.route('/update_locate', methods=['POST'])
def update_locate():
    j = request.get_json(force=True)
    userId = j['userId']
    currentCity = j['currentCity']
    return LocateShareAPI.update_locate_api(userId, currentCity)


@app.route('/login', methods=['POST'])
def login():
    j = request.get_json(force=True)
    return UserManagerAPI.login_api(j['username'], j['password'])


@app.route('/logout', methods=['POST'])
def logout():
    j = request.get_json(force=True)
    logout_user_id = j['userId']
    return UserManagerAPI.logout_api(logout_user_id)


@app.route('/signUp', methods=['POST'])
def signUp():
    j = request.get_json(force=True)
    username = j['username']
    password = j['password']
    fullName = j['fullName']
    avatarUrl = j['avatarUrl']
    gender = j['gender']
    birthYear = j['birthYear']
    currentCity = j['currentCity']
    return UserManagerAPI.signup_api(username, password, fullName, avatarUrl, gender, birthYear, currentCity)


@app.route('/upload/<userId>', methods=['GET', 'POST'])
def upload_file(userId):
    # handle request and store img here
    assert userId == request.view_args['userId']
    print(userId)
    userId = str(userId)
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('static/' + userId + '_' + uploaded_file.filename)
    res = LocateShareAPI.change_ava(userId + '_' + uploaded_file.filename, int(userId))
    res['data'] = userId + '_' + uploaded_file.filename
    return res


if __name__ == "__main__":
    app.run(debug=True)
    arr = os.listdir('./static')
    print(arr)
    for i in arr:
        url_for("static", filename="static/" + i)
