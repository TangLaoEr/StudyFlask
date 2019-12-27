"""
异常捕获errorhandler
"""
from sqlite3 import DatabaseError
from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
	return "index"

@app.route("/demo")
def demo():
	# 主动抛出HTTP指定的错误状态码
	abort(404)
	return "demo"

# 使用装饰器的形式去捕获指定的状态码和异常
@app.errorhandler(404)
def page_not_found(error):
	"""自定义请求错误页面"""
	return "页面异常", 404

@app.errorhandler(DatabaseError)
def databaseNotConnet(error):
	return "数据库出错"




if __name__ == '__main__':
	app.run(debug=True)