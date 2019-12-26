"""
正则路由
"""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 自定义转换器


@app.route('/')
def index():
	return 'index'


#

@app.route('/user/<user_id>')
def user(user_id):
	return user_id


if __name__ == '__main__':
	app.run(debug=True)