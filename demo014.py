"""
请求上下文 request, session
应用上下文 current_app, g
"""
from flask import Flask
from flask import request, session
from flask import current_app, g



app = Flask(__name__)



@app.route('/')
def index():
    print(dir(current_app))
    return "index"

if __name__ == '__main__':
    app.run(debug=True)