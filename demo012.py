"""
session

"""
from flask import Flask, request, make_response, sessions

app = Flask(__name__)


@app.route('/')
def index():
	return "index"




if __name__ == '__main__':
	app.run(debug=True)