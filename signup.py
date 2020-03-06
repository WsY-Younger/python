from flask import Flask
from flask import request
import json
import os

# app = Flask(import_name=__name__, static_url_path='/static', static_folder='/static', template_folder='templates')
app = Flask(import_name=__name__,
            static_url_path='/static', # 配置静态文件的访问 url 前缀
            static_folder='static',    # 配置静态文件的文件夹
            ) 


@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['POST'])
def signin():
    # if request.form['username']=='admin' and request.form['password']=='password':
    #     return '<h3>Hello,admin!</h3>'
    # return '<h3>Bad username or password.</h3>'
    print(request.data)
    data = json.loads(request.data)
    username = data['name']
    password = data['password']
    if username == 'admin' and password == 'password':
        return '{"code": "success"}'
    return '{"code": "error"}'

@app.route('/signup',methods=['POST'])
def signup():
    print(request.data)
    data = json.loads(request.data)
    username = data['name']
    password = data['password']
    jsonString = json.dumps(data)

    isSignUp = False
    users = []
    if(os.path.exists('user.txt')):
        with open('user.txt', 'r') as f:
            usersString = f.read()
            users = json.loads(usersString)
            print(len(users))
            if(len(users) == 0):
                isSignUp = False
            else:
                for user in users:
                    if user['name'] == username:
                        isSignUp = True
                        break
    if(isSignUp):
        dic = {"code": "error", "message": "Username has been signup already"}
        return json.dumps(dic)

    users.append(data)
    jsonString = json.dumps(users)

    with open('user.txt', 'w') as f:
       f.write(jsonString)
    return json.dumps({'code': 'success'})
   



if __name__=='__main__':
    app.run()




