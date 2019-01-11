from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    # user_agent = request.headers.get('User-Agent')
    # # 重定向
    # return redirect('https://www.baidu.com')
    # # 创建一个响应对象，并设置cookie
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response
    # return '<h1>Bad Request</h1>',  400
    # return '<p>Your browser is %s</p>' % user_agent
    # return 'Hello World!'


# 动态路由
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
