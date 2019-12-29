"""
模板代码块
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	user = 'user'
	username = 'tanglaoer'
	my_list = [1, 2, 3, 4]
	my_dict = {
		"id": '1',
		"name": "laowang"
	}
	return render_template('code.html',
							user=user,
							username=username,
							my_list=my_list,
							my_dict=my_dict
							)


if __name__ == '__main__':
	app.run(debug=True)
