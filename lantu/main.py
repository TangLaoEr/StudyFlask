"""
蓝图学习1
"""
from flask import Flask, Blueprint
from order import order
from cart import cart

app = Flask(__name__)
# 3、将蓝图注册到APP上
app.register_blueprint(order)
app.register_blueprint(cart)

@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)