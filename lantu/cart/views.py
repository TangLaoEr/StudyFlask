from . import cart


@cart.route('/cart/list')
def cart_list():
	return "cart_list"