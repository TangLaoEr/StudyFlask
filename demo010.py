"""
请求钩子
"""
from flask import Flask, request

app = Flask(__name__)

# 请求钩子，钩子函数
"""
before_first_request
before_request
after_request
teardown_request
error_handler
"""
@app.before_first_request
def before_first_request():
	"""第一次请求处理函数"""
	# 请求地址是否在黑名单里面
	print('before_first_request')

@app.before_request
def before_request():
	"""请求之前"""
	print('before_request')

@app.after_request
def after_request(response):
	"""请求函数之后会调用，并且函数里面接收一个参数response，还需要将响应返回"""
	# 对响应进行统一
	print('after_request')
	return response


@app.teardown_request
def teardown_request(error):
	"""在请求函数之后会执行，如果请求的函数报有异常，会把具体的异常传入此函数。"""

	# 如果没有异常，那么此函数就在视图函数之后正常执行
	print('teardown_request')
	print(error)  # 异常

@app.route('/')
def index():
	return "index"


if __name__ == '__main__':
	app.run(debug=True)