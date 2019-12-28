"""
session 依赖cookie
"""
from flask import Flask, session

"""
每次重新设置的session加密后产生不一样的session字符串序列。
"""

app = Flask(__name__)
app.secret_key = "tanglaoer"

@app.route('/')
def index():
	user_id = session['user_id']
	user_name = session['user_name']
	return "index"

@app.route('/login')
def login():
	"""写入session"""
	session['user_id'] = "1"
	session['user_name'] = "laowang"
	return "success"


@app.route('/logout')
def logout():
	session.clear()
	return "logout"

if __name__ == '__main__':
	app.run(debug=True)