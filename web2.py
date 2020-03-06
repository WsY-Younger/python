from flask import Flask
from flask import request

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
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__=='__main__':
    app.run()




