from flask import Blueprint

cart = Blueprint('cart', __name__)

# 需要引用路由
# 不然，不会调用到view.py文件里面的路由注册
from .views import *