"""
sqlalchemy2 案例一
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://tang:123456@47.106.82.47:3306/booktest'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Author(db.Model):
	"""作者"""
	__tablename__ = "authors"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)  # 唯一
	# 定义属性， 以便作者模型可以直接通过该属性访问其多的一方的数据（书的数据）
	# backref 给Book也添加一个可以访问author的睡醒，可以通过book.author 获取book所对应的作者信息
	books = db.relationship("Book", backref='author')

class Book(db.Model):
	"""书籍"""
	__tablename__ = "books"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True) # unique 唯一
	# 记录一的一方的id作为外键
	author_id = db.Column(db.Integer, db.ForeignKey(Author.id))


@app.route('/')
def index():
	return "index"


if __name__ == '__main__':
	# 删除所有的表
	db.drop_all()
	# 创建所有的表
	db.create_all()
	au1 = Author(name='老王')
	au2 = Author(name='老伊')
	au3 = Author(name='老刘')
	db.session.add_all([au1, au2, au3])
	db.session.commit()

	bk1 = Book(name='老王回忆录',author_id=1)
	bk2 = Book(name='城南旧事', author_id=1)
	bk3 = Book(name='啊Q正传', author_id=2)
	bk4 = Book(name='白夜行', author_id=2)
	bk5 = Book(name='解忧杂货店', author_id=3)
	bk6 = Book(name='嫌疑人', author_id=3)
	db.session.add_all([bk1, bk2, bk3, bk4, bk5, bk6])
	db.session.commit()

	app.run(debug=True)

