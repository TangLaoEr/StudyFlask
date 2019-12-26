"""
正则路由1
"""
from flask import Flask
# 0.导入相关的模块
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 1.自定义转换器
class RegexConverter(BaseConverter):
	"""自定义转换器"""

	# 修改类的regex属性
	regex = "[0-9]{6}"

# 2.将自定义的转换器添加到系统默认的转换器列表中
app.url_map.converters['re'] = RegexConverter


@app.route('/')
def index():
	return 'index'


#

@app.route('/user/<re:user_id>')
def user(user_id):
	return user_id


if __name__ == '__main__':
	app.run(debug=True)