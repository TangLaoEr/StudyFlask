"""
自定义状态码
"""
from flask import Flask

app = Flask(__name__)

# 常用配置可以直接通过app来. 出来属性


@app.route('/')
def index():
	return "index"



# 返回响应的状态码
@app.route('/statuc')
def demo():
	# 第二个参数为状态码
	return 'demo666', 666


if __name__ == '__main__':
	app.run(debug=True)