"""
模板继承
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/demo')
def demo():
    return render_template('demo.html')

if __name__ == '__main__':
    app.run(debug=True)