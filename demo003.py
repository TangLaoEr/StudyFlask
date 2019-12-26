"""
路由配置
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return "hello world"

@app.route('/demo1')
def demo():
	return "demo"

# 指定路由参数类型
# 给路由添加参数，格式就是<参数名>
# 并且视图函数需要接收这个参数
@app.route('/user/<int:user_id>')
def user(user_id):
	print(type(user_id))
	return str(user_id)

# 指定请求的方式
@app.route('/demo3/', methods=['GET','POST'])
def demo3():
	json_dict = {
		"name":"laowang",
		"age":18,
	}
	# return "demo3"
	# 利用flask自带的jsonify比json的模块好，jsonify会帮助我们封装好响应内容，比如响应头部content-type:json
	return jsonify(json_dict)

app.debug = True

if __name__ == '__main__':
	app.run(debug=True)