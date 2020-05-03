from flask import Flask
from flask import request
import json
import os

app = Flask(import_name = __name__,
            static_url_path='/static',
            static_folder='static',)

@app.route('/',methods=['GET'])
def home():
    return
@app.route('/d',methods=['POST'])
def login():
    print(request.data)
    data = json.loads(request.data)
    username =data['name']
    password =data['password'] 
    findUser = False
    selectUser = {}
    if (os.path.exists('user.txt')):
        with open('user.txt','r') as f:
            userString = f.read()
            users = json.loads(userString)
            if (len(users) != 0):
                for user in users:
                    if user['name'] == username:
                        selectUser = user
                        findUser = True
                        break
    if findUser == False:
        dic = {"code":"error","message":"请先注册"}
        return json.dumps(dic)
    
    if selectUser['password'] != password:
        dic = {"code":"error","message":"密码错误"}
        return json.dumps(dic)
    return json.dumps({"code":"success"})

@app.route('/z',methods = ['POST'])
def signup():
    print(request.data)
    data = json.loads(request.data)
    username = data['name']
    password = data['password']
    jsonString = json.dumps(data)


    issignup = False
    users = []
    if (os.path.exists('user.txt')):
        with open('user.txt','r') as f:
            userString = f.read()
            users = json.loads(userString)
            print(len(users))
            if(len(users) == 0):
                isSignup = False
            else :
                for user in users:
                    if user['name'] == username:
                        isSignup = True
                        break

    if(issignup):
        dic = {"code":"error","message":"已注册"}
        return json.dumps(dic)

    users.append(data)
    jsonString = json.dumps(users)

    with open('user.txt','w') as f:
        f.write(jsonString)
    return json.dumps({"code":"success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')




    

