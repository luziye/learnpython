# -*- encoding=UTF-8 -*-

from flask_script import Manager
from c2 import app

manager=Manager(app)

@manager.option('-n','--name',dest='name',default='luziye')
def hello(name):
    print 'hello',name

@manager.command
def init_database():
    '''初始化数据库'''
    print 'database...'

if __name__=='__main__':
    manager.run()