"""
代码控制块
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "demo3.html"

if __name__ == '__main__':
    app.run(debug=True)