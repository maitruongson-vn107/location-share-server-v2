from config import db
from datetime import date
from KeyAPI import add_key

cursor = db.cursor()

online_users = {0}


def login_api(username, hashed_password):
    sql = "SELECT * FROM User WHERE username = %s AND password = %s"
    params = (username, hashed_password)
    cursor.execute(sql, params)
    user = cursor.fetchone()
    today = date.today()
    yearNow = today.year
    if user is None:
        return {"msg": "fail", "data": 'fail'}
    data = {
        "userId": user[0],
        "username": user[1],
        "password": user[2],
        "fullName": user[3],
        "avatarUrl": user[4],
        "gender": user[5],
        "age": yearNow - user[6],
        "currentCity": user[7]
    }
    if user[0] not in online_users:
        online_users.add(user[0])
    return {"msg": "success", "data": data}


def logout_api(userId):
    if userId in online_users:
        online_users.remove(userId)
        return {"msg": "success", "data": None}
    else:
        return {"msg": "fail", "data": None}


def signup_api(username, password, fullName, avatarUrl, gender, birthYear, currentCity):
    if username is None or password is None or \
            fullName is None or gender is None or \
            currentCity is None:
        return {"msg": "fail"}
    sql = "SELECT * FROM User WHERE username = %s"
    params = (username,)
    cursor.execute(sql, params)
    existing_user = cursor.fetchone()
    if existing_user is None:
        sql = "INSERT INTO User(username, password, fullName, avatarUrl, gender, birthYear, currentCity, counter) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, 0)"
        params = (username, password, fullName, avatarUrl, gender, birthYear, currentCity)
        try:
            cursor.execute(sql, params)
            db.commit()
            userId = cursor.getlastrowid()
            today = date.today()
            yearNow = today.year
            data = {
                "userId": userId,
                "username": username,
                "password": password,
                "fullName": fullName,
                "avatarUrl": avatarUrl,
                "gender": gender,
                "age": yearNow - birthYear,
                "currentCity": currentCity
            }
            sql1 = "SELECT * FROM User WHERE UserId != %s"
            params1 = (userId, )
            cursor.execute(sql1, params1)
            users = cursor.fetchall()
            for u in users:
                b = False
                while not b:
                    b = add_key(u[0], userId)

            return {"msg": "success", "data": data}
        except:
            return {"msg": "fail", "data": None}
    else:
        return {"msg": "fail", "data": None}
