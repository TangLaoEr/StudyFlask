"""
flask_script扩展
命令行管理
"""
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
# 1.创建manager与app进行关联
manager = Manager(app)

@app.route('/')
def index():
    return "index222"

if __name__ == '__main__':
    # 2.使用manager启动服务
    manager.run()
