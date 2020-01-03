"""
数据库ORM操作
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://tang:123456@47.106.82.47:3306/StudentFlask'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "Role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # backref 在这行代码的作用是：给前面的 User添加一个属性， 名字叫backref的值
    # 以便可以直接通过user.role方法到一 的一方的数据

    # 一跟多的互相访问
    users = db.relationship('User', backref='role')

    """
    user = User.query.get(1)
    user.role
    
    role = Role.query.get(1)
    role.users
    """

    def __repr__(self):
        return "Role %d %s" %(self.id, self.name)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(64), unique=True)
    # 外键关系
    # 放在多的一面
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return "User %d %s" %(self.id, self.name)


@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    db.session.add_all([ro1, ro2])
    db.session.commit()

    user1 = User(name='laowang')
    user1.role_id = 1
    user2 = User(name='laoli')
    user2.role_id = 1
    user3 = User(name='laozhang')
    db.session.add_all([user1, user2, user3])

    # 提交
    db.session.commit()
    app.run(debug=True)