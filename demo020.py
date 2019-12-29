"""
过滤器传参数
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_dict_list = [
        {'name':'laoer','age':20},
        {'name':'laosan','age':18},
    ]

    return render_template('guolvqi.html', my_dict_list=my_dict_list)

if __name__ == '__main__':
    app.run(debug=True)