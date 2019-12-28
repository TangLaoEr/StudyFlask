"""
cookie and session
"""
from flask import Flask, sessions, make_response, request

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
	response.set_cookie('user_id', '1', max_age=3600)  # 秒为单位
	response.set_cookie('user_name', 'laowang')
	return response



@app.route('/')
def index():
	"""首页"""

	# 在请求中获取cookie
	user_id = request.cookies.get('user_id')
	user_name = request.cookies.get('user_name')
	print(user_id)
	print(user_name)
	return "index"

if __name__ == '__main__':
	app.run(debug=True)