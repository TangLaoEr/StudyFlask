"""
数据库ORM操作
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:123456@47.106.82.47:3306/leetcode'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = False

db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = "Role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return "Role %d %s" %(self.id, self.name)


@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    app.run(debug=True)