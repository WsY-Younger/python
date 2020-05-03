from flask import Flask
from flask import request
import json
import os

app = Flask(import_name = __name__,
            fold_url_path='/fold',
            fold_folder='fold',)


@app.route('/z',method = ['POST'])
def signup():
    print(request.data)
    data = json.loads(request.data)
    username = data['name']
    password = data['password']
    jsonString = json.dumps(data)


    issignup = False
    users = []
    if (os.path.exist('user.txt')):
        with open('user.txt','r') as f:
            userString = f.read()
            users = json.loads(usersString)
            print(len(users))
            if(len(users) == 0):
                isSignup = False
            else :
                for user in users:
                    if user['name'] == username:
                        isSignup = True
                        break

    if(isSignup):
        dic = {"code":"error","message":"已注册"}
        return json.dumps(dic)

    users.append(data)
    jsonString = json.dumps(users)

    with open('user.txt','w') as f:
        f.write(jsonString)
    return json.dumps({"code":"success"})


if __name__ == '__main__':
    app.run()