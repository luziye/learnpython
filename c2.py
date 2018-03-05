# -*- encoding=UTF-8 -*-
from flask import Flask, render_template, request, make_response, flash, get_flashed_messages
from logging.handlers import RotatingFileHandler
import logging
app = Flask(__name__)
app.secret_key = 'lzy'


@app.route('/index/')
@app.route('/')
def index():
    res = ''
    for msg, cat in get_flashed_messages(with_categories=True):
        res = res + msg + cat + '<br>'
    res += 'hello'
    return res


@app.route('/profile/<int:uid>/')
def profile(uid):
    colors = ('red', 'green', 'blue')
    infos = {'nowcoder': 'abc', 'google': 'xyz'}
    return render_template("profile.html", uid=uid, colors=colors, infos=infos)


@app.errorhandler(404)
def page_not_found(error):
    print error
    return render_template('not_found.html', url=request.url)


@app.route('/login/')
def login():
    flash('登录成功', 'info')
    return 'ok'

@app.route('/log/<level>/<msg>/')
def log(level,msg):
    dict={'warn':logging.WARN,'error':logging.ERROR,'info':logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level],msg)
    return 'logged:'+msg


if __name__ == '__main__':
    app.run(debug=True)
