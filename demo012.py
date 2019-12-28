"""
session 状态保持
"""
from flask import Flask, request, make_response, session

app = Flask(__name__)

app.secret_key = "tanglaoer"

@app.route('/')
def index():
	return "index"

@app.route('/login')
def login():
	"""login"""
	session['user_id'] = 1
	session['user_name'] = 'laowang'
	return "login"


@app.route('/logout')
def logout():
	return "logout"


if __name__ == '__main__':
	app.run(debug=True)