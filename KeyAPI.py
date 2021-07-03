import random

from config import db

cursor = db.cursor()


def generate_common_key():
    i = 1
    common_key = str(random.randint(1, 3))
    while i < 10:
        common_key = common_key + str(random.randint(0, 9))
        i = i + 1
    return common_key


def add_key(userId1, userId2):
    sql1 = "SELECT * FROM CommonKey WHERE UserId1 = %s AND UserId2 = %s"
    params1 = (userId1, userId2)
    cursor.execute(sql1, params1)
    existing_key = cursor.fetchone()
    if existing_key is not None:
        return {"msg": "fail", "data": None}
    else:
        common_key = generate_common_key()
        sql2 = "INSERT INTO CommonKey(userId1, userId2, commonKey) VALUES (%s, %s, %s)"
        params2 = (userId1, userId2, common_key)
        cursor.execute(sql2, params2)
        db.commit()
        return {
            "msg": "success",
            "data": {
                "userId1": userId1,
                "userId2": userId2
            }
        }



