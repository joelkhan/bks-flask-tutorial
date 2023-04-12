from flask import Flask
from flask import url_for


app = Flask(__name__)

@app.route('/index')
@app.route('/')
@app.route('/home')
@app.route('/index2')
def hello():
    msg = u'<h1>欢迎来到我的 Watchlist！</h1>' 
    msg += '<h1>Hello Totoro!</h1>'
    msg += '<img src="http://helloflask.com/totoro.gif">'
    return msg + '<p>Welcome to My Watchlist!</p>'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name


@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（ 请在命令行窗口查看输出的 URL） ：
    print(url_for('hello')) # 输出： /
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli')) # 输出： /user/greyli
    print(url_for('user_page', name='peter')) # 输出： /user/peter
    print(url_for('test_url_for')) # 输出： /test
    # 下面这个调用传入了多余的关键字参数， 它们会被作为查询字符串附加到 URL后面。
    print(url_for('test_url_for', num=2)) # 输出： /test?num=2
    return 'Test page'


