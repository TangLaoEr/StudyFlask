"""
重定向
"""
from flask import Flask,redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
	# redirect 参数是str
	# url_for 参数为函数名转换为url   一般redirect结合url_for使用
	# return redirect(url_for('index'))
	return redirect('https://wwww.ba idu.com')

if __name__ == '__main__':
	app.run(debug=True)