"""
数据库多对多案例 db.Table  secondary lazy 关键字
 """
from flask import Flask, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
app.secret_key = "%s" % uuid.uuid4()
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://tang:123456@47.106.82.47:3306/booktest'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

"""
http://www.pythondoc.com/flask-sqlalchemy/models.html#many-to-many
官方案例
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
"""

# 创建一个单独的表
# 不需要这张表的模型, 不需要创建类，只需要通过Table
tb_Stundent_Course = db.Table(
	# 添加这张表的字段
	"student_course",
	db.Column("student_id", db.Integer, db.ForeignKey("student.id")),
	db.Column("course_id", db.Integer, db.ForeignKey("course.id"))
)


class Student(db.Model):
	"""学生表"""
	id = db.Column(db.Integer, primary_key=True)
	# 名字
	name = db.Column(db.String(64), unique=True)
	# 当前学生选修的课程
	courses = db.relationship('Course',
							  secondary=tb_Stundent_Course,
							  lazy="dynamic", # 性能相关
							  backref=db.backref("students", lazy="dynamic"))

"""
不加lazy是列表，里面是具体数据。
加lazy是被使用的时候才加载。


用到才查询，节省性能跟django里面的两个orm字段一样
lazy = "dynamic"
# 如果不指定该值，那么当 student 查询数据之后，courses 就已经有值(已经从Course表里面把数据查询出来了)。
# 如果指定该值，那么当 student 查询数据之后，courses 并没有具体的值，而只是查询对象
# 如果只是查询对象，那么就可以在用的时候再去数据库查询，避免不必要的查询操作，影响性能。
现在只是stu1.courses 这样子节省性能

要是想cou1.students也可以节省性能，可以指定backref = db.backref('students', lazy="dynamic")
"""


class Course(db.Model):
	"""课程表"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)


@app.route('/')
def index():
	return "index"


if __name__ == '__main__':
	db.drop_all()  # 只会删除这里类名对应的表
	db.create_all()
	stu1 = Student(name='张三')
	stu2 = Student(name='李四')
	stu3 = Student(name='王五')


	course1 = Course(name='物理')
	course2 = Course(name='化学')
	course3 = Course(name='语文')
	course4 = Course(name='数学')

	stu1.courses = [course1, course2]
	stu2.courses = [course2, course3]
	stu3.courses = [course3, course4]
	db.session.add_all([stu1, stu2, stu3])
	db.session.add_all([course1, course2, course3, course4])

	db.session.commit()
	app.run(debug=True)
