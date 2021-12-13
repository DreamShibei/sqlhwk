import os
import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import config
from mysql import Mysql

# GLOBAL VARIABLE
pageNum = 4

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
#引入配置文件必须在创建数据库连接之前

SQLALCHEMY_DATABASE_URI = "mysql:///root:{pwd}@127.0.0.1:3306/henanopera"
# "数据库：//用户名：密码@host：port/数据库名称"

SQLALCHEMY_TRACK_MODIFICATIONS = False
# 这一行不加会有警告

if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    page = request.args.get('page')
    print(page)
    if not page or int(page) == 0:
        page = 1
    db = Mysql()
    items = db.getMovies(page)
    num = db.getNum()
    page_range = range(max(1,int(page)-1), (min(int((num-1)/pageNum)+2,int(page) + 2)))
    return render_template('video.html', items=items, page=int(page), prange=page_range)

@app.route('/text')
def text():
    page = request.args.get('page')
    print(page)
    if not page or int(page) == 0:
        page = 1
    db = Mysql()
    items = db.getText(page)
    num = db.getNum()
    page_range = range(max(1,int(page)-1), (min(int((num-1)/pageNum)+2,int(page) + 2)))
    return render_template('text.html', items=items, page=int(page), prange=page_range)

@app.route('/picture')
def picture():
    page = request.args.get('page')
    print(page)
    if not page or int(page) == 0:
        page = 1
    db = Mysql()
    items = db.getPicture(page)
    num = db.getNum()
    page_range = range(max(1,int(page)-1), (min(int((num-1)/pageNum)+2,int(page) + 2)))
    return render_template('picture.html', items=items, page=int(page), prange=page_range)

@app.route('/music')
def music():
    page = request.args.get('page')
    print(page)
    if not page or int(page) == 0:
        page = 1
    db = Mysql()
    items = db.getMusic(page)
    num = db.getNum()
    page_range = range(max(1,int(page)-1), (min(int((num-1)/pageNum)+2,int(page) + 2)))
    return render_template('music.html', items=items, page=int(page), prange=page_range)
