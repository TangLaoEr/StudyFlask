"""
自定义过滤器
"""
from flask import Flask, render_template

app = Flask(__name__)

"""
过滤器原本就是一个函数
自定义过滤器：两种方式
1、通过装饰器@app.template_filter
2、通过函数app.add_template_filter, 添加到app中
"""

# 方式1
def do_lireverse2(li):
    temp = list(li)
    temp.reverse()
    return temp

app.add_template_filter(do_lireverse2, 'lireverse2')


# 方式2
@app.template_filter('lireverse')
def do_lireverse(li):
    from copy import copy
    temp = copy(li)
    temp.reverse()
    return temp

@app.route('/')
def index():
    # 使用自定义的过滤器
    my_list = [1,2,3,4,5]
    return render_template('my_filter.html',
                           my_list=my_list)

if __name__ == '__main__':
    app.run(debug=True)