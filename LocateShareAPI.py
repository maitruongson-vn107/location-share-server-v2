import datetime
import random


from config import db
import UserManagerAPI
import requests
cursor = db.cursor()


def change_ava(avaUrl, userId):

    sql = "UPDATE User SET avatarUrl = %s WHERE userId = %s"
    params = (avaUrl, userId)
    try:
        cursor.execute(sql, params)
        db.commit()
        return {"msg": "success", "data": None}
    except:
        return {"msg": "fail", "data": None}

def get_client_url(client_id:int):
    port = 5000 + client_id
    return 'http://127.0.0.1:'+ str(port) +'/'
def search_api(userId):
    #get all user
    try:
        sql = "SELECT u.*, k.commonKey FROM User u, CommonKey k " \
              "WHERE (u.userId = k.userId1 AND k.userId2 = %s) OR (u.userId = k.userId2 AND k.userId1 = %s) " \
              "ORDER BY u.userId ASC"
        params = (userId, userId)
        cursor.execute(sql, params)
        results = cursor.fetchall()
        
    except:
        return {"msg": "fail", "data": None}
    data = []
    # Getting results
    
    for u in results:
        #for each online user
        if u[0] in UserManagerAPI.online_users:

            # Update_get counter and get common_key with current user and other online user
            counter = u[-2]
            counter = counter + 1
            update_counter_api(u[0], counter)
            common_key = int(u[-1])

            # Alice and Bob send encrypted position
            body_data = {"common_key":common_key,"counter":counter,"role":'bob'}
            bob_res = requests.post(get_client_url(u[0]) + 'encrypt_pos',json = body_data).json()

            body_data = {"common_key":common_key,"counter":counter,"role":'alice'}
            alice_res = requests.post(get_client_url(userId) + 'encrypt_pos',json = body_data).json()

            #now sam doesn't know about position
            x_a = alice_res['x_a']
            r = bob_res['r']

            x_b = bob_res['x_b']
            x = r * x_a - x_b

            body_data = {'x':x}
            #send x to alice to check whether bob and alice in the same position
            check = requests.post(get_client_url(userId) + 'check',json = body_data).json()['check']
            # Get result list
            if check:
                today = datetime.date.today()
                yearNow = today.year
                data.append({
                    "fullName": u[3],
                    "age": yearNow - u[6],
                    "gender": u[5],
                    "avatarUrl": u[4]
                })

    return {"msg": "success", "data": data}



def update_counter_api(userId, counter):
    sql = "UPDATE User SET counter = %s WHERE userId = %s"
    params = (counter, userId)
    try:
        cursor.execute(sql, params)
        db.commit()
        return {
            "msg": "success",
            "data": {"userId": userId,
                     "counter": counter}
            }
    except:
        return {"msg": "fail", "data": None}
