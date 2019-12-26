"""
flask创建时候的参数
"""
from flask import Flask

# 第一个参数指代Flask所对应的模块，其可以决定静态文件从哪个位置开始找。
app = Flask(__name__,
			static_url_path='/static', 	# 表示静态文件访问的路径，可以修改为任意的 /xxx
			static_folder='static',    # 静态文件存放的目录
			template_folder='templates' # 表示模板文件存放的目录
			)


# 添加想要的配置
# 三种配置方式
# 三种模式
"""
app.config.from_object()  # 从对象中
app.config.from_pyfile()  # 从py文件中
app.config.from_envvar()  # 从环境变量中
"""

# 从对象中加载配置
# class Config(object):
# 	DEBUG = True

# 配置
# app.config.from_object(Config)  # 从对象中读取


# 从文件中加载配置
# 当前文件目录下的创建该文件
# app.config.from_pyfile('config.ini')


# 从环境变量中加载
# 在edit configurations 中添加环境变量
# app.config.from_envvar('ENVCONFIG')



"""
app.config 是字典的子类
app.config['debug']
"""

# 一些常用的配置，可以直接通过app.来配置
# eg: app.debug = True
app.debug = True
app.config['DEBUG'] = True  # 等同于上面一句


@app.route('/')
def index():
	# print(app.config)
	print(isinstance(app.config, dict))
	return "hello world"

if __name__ == '__main__':
	app.run(debug=True,port=8000)