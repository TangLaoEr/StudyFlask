"""
flask_wtf扩展
"""
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, EqualTo

app = Flask(__name__)
app.secret_key = "tanglaoer"
app.config['WTF_CSRF_ENABLED'] = True

class RegisterForm(FlaskForm):
	username = StringField('用户名:', render_kw={'placeholder':'占位符'}, validators=[InputRequired('请输入用户名')])
	password = StringField('密码:', validators=[InputRequired('请输入密码')])
	password2 = StringField('确认密码:', validators=[InputRequired('请输入确认密码'), EqualTo('password', '两次密码要一致')])
	submit = SubmitField('注册')

@app.route('/')
def index():
	return "index"


"""
闪现需要借助session
"""

@app.route('/register2', methods=['GET', 'POST'])
def register2():
	if request.method == "POST":
		username = request.form.get('username')
		password = request.form.get('password')
		password2 = request.form.get('password2')
		if not all([username, password, password2]):
			flash("参数不足")  # 闪现

		elif password2 != password:
			flash("两次密码不一致")
		else:
			print(username, password, password2)
			return 'success'

	return render_template('register2.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	"""利用flask_wtf"""
	register_form = RegisterForm()

	# 使用wtf 表单帮助我们做验证,
	if register_form.validate_on_submit():
		# 验证通过,执行注册逻辑
		username = request.form.get('username') # 或者通过这种方式 register_form.username.data
		password = request.form.get('password')
		password2 = request.form.get('password2')
		print(username, password, password2)
		return 'success'
	else:
		if request.method == "POST":
			flash('参数错误')

	return render_template('register.html', form=register_form)

if __name__ == '__main__':
	app.run(debug=True)
