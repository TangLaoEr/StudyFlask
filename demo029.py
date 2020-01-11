"""
数据库迁移操作, flask_script flask_migrate
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# MigrateCommand 迁移的命令
# 需要借助flask_script 库作用

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://tang:123456@47.106.82.47:3306/StudentFlask'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.debug = True

db = SQLAlchemy(app)

# 使用迁移类将应用和数据库连接对象保存起来
Migrate(app, db)
# 创建终端命令的对象
manager = Manager(app)
# 将数据库的迁移命令添加到manager中, 一般是db
manager.add_command('db', MigrateCommand)

class Role(db.Model):
	__tablename__ = "Role"
	id = db.Column(db.Integer, primary_key=True)
	nick_name = db.Column(db.String(64), unique=True)
	# backref 在这行代码的作用是：给前面的 User添加一个属性， 名字叫backref的值
	# 以便可以直接通过user.role方法到一 的一方的数据

	# 一跟多的互相访问
	users = db.relationship('User', backref='role')

	# 新增字段
	title = db.Column(db.String(64))
	heigth = db.Column(db.Integer)

	"""
	user = User.query.get(1)
	user.role

	role = Role.query.get(1)
	role.users
	"""

	def __repr__(self):
		return "Role %d %s" % (self.id, self.name)


class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	# 外键关系
	# 放在多的一面
	role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

	def __repr__(self):
		return "User %d %s" % (self.id, self.name)


@app.route('/')
def index():
	return "index"


if __name__ == '__main__':
	manager.run()

"""
$python demo029.py aaa init   # aaa 是自己定义的， 会创建一个目录migrations
$python demo029.py aaa migrate -m"initial"

总结迁移的命令
db = manager.add_command('db', MigrateCommand)
1、迁移初始化 python xxx.py db init  # 只有第一次的时候需要

2、生成迁移版本文件 python xxx.py db migrate -m "xxxx"  # 迁移生成并记录log
3、执行迁移(往上迁移) python xxx.py db upgrate    # 这里才会生成表

# 案例一 添加字段需要 执行 2 3 步骤
python xxx.py db migrate -m "xxx"
python xxx.py db upgrade 


命令行命令大全：
python 文件 db init
python 文件 db migrate -m "版本名（注释）"
python 文件 db upgrade 然后观察表结构
python 文件 db history 查看版本号
python 文件 db downgrade
"""