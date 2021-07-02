# from flask import Flask, render_template, request
import requests

# app = Flask(__name__)

# @app.route("/upload", methods = ["GET", "POST"])
# def upload_file():
#     # handle request and store img here
#     uploaded_file = request.files["file"]
#     if uploaded_file.filename != "":
#         uploaded_file.save("static/"+uploaded_file.filename)
    
#     return	{"a":"a"}
# if __name__ == "__main__":
#    app.run(debug = True)
'''
TESTING API for LocationShareServer
1. Test API Login: data1 (có thể test nhiều users -> nhiều users online cùng lúc)

2. Test API Signup: data2

3. Test API Update Location: data3

4. Test API Search: data4 -> chỉ trả về danh sách những người online + ở gần 
'''

# data1 = {"username": "sonmt", "password": "fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603"}
# response1 = requests.post("http://127.0.0.1:5000/login", json=data1).json()
# print(response1)
#
# data1 = {"username": "bot1", "password": "fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603"}
# response1 = requests.post("http://127.0.0.1:5000/login", json=data1).json()
# print(response1)
#
# data1 = {"username": "bot2", "password": "fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603"}
# response1 = requests.post("http://127.0.0.1:5000/login", json=data1).json()
# print(response1)
#
# data2 = {"username": "son2", "password": "fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603",
#          "birthYear": 1999, "avatarUrl": "ava.png", "currentCity": "3", "gender": 1, "fullName": "MTS"}
# response2 = requests.post("http://127.0.0.1:5000/signUp", json=data2).json()
# print(response2)
#
# data3 = {"userId": 1, "currentCity": "3"}
# response3 = requests.post("http://127.0.0.1:5000/update_locate", json=data3).json()
# print(response3)
#
# data4 = {"userId": 1, "currentCity": "3"}
# response4 = requests.get("http://127.0.0.1:5000/search", json=data4).json()
# print(response4)

