from flask import Blueprint

# 1 初始化蓝图
order = Blueprint('order', __name__)


# 2 使用蓝图去注册路由url
@order.route('/order/list')
def order_list():
	return 'order'

