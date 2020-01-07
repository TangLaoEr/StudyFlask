"""
数据库sqlalchemy 事务操作
"""
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import uuid

app = Flask(__name__)
app.secret_key = "%s"%uuid.uuid4()
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

# 表单
class AddBookForm(FlaskForm):
	"""自定义添加书籍表单"""
	author = StringField('作者', validators=[InputRequired('请输入书名')])
	book = StringField('书名', validators=[InputRequired("请输入作者名")])
	submit = SubmitField("添加")

@app.route('/', methods=['GET', 'POST'])
def index():
	"""首页"""
	book_form = AddBookForm()
	if book_form.validate_on_submit():
		"""post请求"""
		author_name = book_form.author.data
		book_name = book_form.book.data

		author = Author.query.filter(Author.name == author_name).first()
		if not author:
			try:
				author = Author(name=author_name)
				db.session.add(author)
				db.session.commit()

				book = Book(name=book_name, author_id=author.id)
				db.session.add(book)
				db.session.commit()
			except Exception as e:
				db.session.rollback()  # 回滚
				print(e)
				flash('添加失败')

		else:
			book = Book.query.filter(Book.name == book_name).first()
			if not book:
				try:
					book = Book(name=book_name, author_id=author.id)
					db.session.add(book)
					db.session.commit()
				except Exception as e:
					print(e)
					flash('添加失败')
			else:
				flash('已存在')
	else:
		if request.method == "POST":
			flash("参数错误")


	# 1/ 查询数据
	authors = Author.query.all()

	return render_template('bookDemo.html', authors=authors, form=book_form)

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
	"""删除book"""
	book = None
	try:
		book = Book.query.get(book_id)

	except Exception as e:
		print(e)
		return '查询错误'

	if not book:
		return "书籍不存在"

	try:
		db.session.delete(book)
		db.session.commit()
	except Exception as e:
		print(e)

	return redirect(url_for("index"))

@app.route('/delete_author/<author_id>')
def delete_author(author_id):
	"""删除作者"""
	try:
		author = Author.query.get(author_id)
	except Exception as e:
		print(e)
		return '查询错误'

	if not author:
		return "作者不存在"

	#todo: 删除作者及其所有的书籍
	try:
		# 删除作者所有的书籍
		Book.query.filter(Book.author_id == author_id).delete()
		# 删除作者
		db.session.delete(author)
		db.session.commit()

	except Exception as e:
		print(e)
		db.session.rollback()  # 回滚
		return "删除失败"
	return redirect(url_for('index'))



if __name__ == '__main__':
	# 删除所有的表
	# db.drop_all()
	# # 创建所有的表
	# db.create_all()
	# au1 = Author(name='老王')
	# au2 = Author(name='老伊')
	# au3 = Author(name='老刘')
	# db.session.add_all([au1, au2, au3])
	# db.session.commit()
	#
	# bk1 = Book(name='老王回忆录',author_id=1)
	# bk2 = Book(name='城南旧事', author_id=1)
	# bk3 = Book(name='啊Q正传', author_id=2)
	# bk4 = Book(name='白夜行', author_id=2)
	# bk5 = Book(name='解忧杂货店', author_id=3)
	# bk6 = Book(name='嫌疑人', author_id=3)
	# db.session.add_all([bk1, bk2, bk3, bk4, bk5, bk6])
	# db.session.commit()

	app.run(debug=True)

