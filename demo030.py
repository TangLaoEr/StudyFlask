"""
信号机制
使用一个第三方库的信号
信号依赖 blinker 库

"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    app.run(debug=True)


"""
信号步骤
# 订阅谁发的信号
@信号.connect_via(app)
"""