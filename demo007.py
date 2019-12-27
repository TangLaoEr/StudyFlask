"""
正则路由2
"""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class MyConverter(BaseConverter):
	"""自定义正则表达式"""

	# 可以让自己在路由上面写上要匹配的正则表达式
	# args 接收传入的参数
	def __init__(self, url_map,  *args):
		super(MyConverter, self).__init__(url_map)
		# 参数
		self.regex = args[0]

app.url_map.converters['re'] = MyConverter

@app.route("/")
def index():
	return "index"


@app.route('/user/<re("[0-9]{5}"):user_id>')
def demo(user_id):
	return user_id


if __name__ == '__main__':
	app.run(debug=True)
