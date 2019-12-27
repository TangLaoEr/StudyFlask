"""
正则转换器3to_python,to_rul
"""
from flask import Flask, redirect, url_for
from werkzeug.routing import  BaseConverter

app = Flask(__name__)

class MyConverter(BaseConverter):
	def __init__(self, url_map, *args):
		super(MyConverter, self).__init__(url_map)
		self.regex = args[0] if args else None

	def to_python(self, value):
		return int(value)

class ListConverter(BaseConverter):
	"""自定义转换器"""
	regex = "(\\d+,?)+\\d$"  # 用来匹配接收

	def to_python(self, value):
		"""当匹配到参数之后,对参数做进一步处理之后，再返回给视图函数中"""
		return value.split(',')

	def to_url(self, value):
		"""使用url_for函数的时候，对视图函数传的参数进行处理，处理完毕之后以便能够进行路由匹配"""
		# 进行字符串整数的转换
		return ",".join(str(i) for i in value)


app.url_map.converters['re'] = MyConverter
app.url_map.converters['listre'] = ListConverter

@app.route("/")
def index():
	return "index"


@app.route('/user/<re:user_id>')
def user(user_id):
	return user_id


@app.route("/users/<listre:user_ids>")
def users(user_ids):
	"""使接收到的user_ids为列表1，2，3，4"""
	return "%s" % user_ids

@app.route("/demo")
def demo():
	return redirect(url_for('users', user_ids=[1,2,3,4]))


if __name__ == '__main__':
	app.run(debug=True)
