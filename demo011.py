"""
cookie and session
"""
from flask import Flask, sessions, Request, Response, make_response

app = Flask(__name__)

# @app.route("/login")
# def login():
# 	Request.args
# 	Request.date
# 	Request.form
	# print(Request.form)
	# response = Response("login.html")
	#
	# response.set_cookie('user_id', "1")
	# response.set_cookie('user_name', "laowang")
	# return response

@app.route("/login")
def login():
	"""登录函数"""

	# 生成一个响应的函数
	response = make_response('success')
	response.set_cookie('user_id', '1')
	response.set_cookie('user_name', 'laowang')
	return response


@app.route('/')
def index():

	return "index"

if __name__ == '__main__':
	app.run(debug=True)