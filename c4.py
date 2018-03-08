# -*- encoding=UTF-8 -*-
import os
class Test(object):
    nis=0
    def __init__(self,name):
        self.name=name
        Test.nis+=1

a='1'
b={'a':1,'b':2,'c':3}
c=True

d={x*x for x in range(0,10,2)}


if __name__=='__main__':
    # print Test.nis
    # t1=Test('jack')
    # print Test.nis
    # t2=Test('alice')
    # print t1.name,Test.nis
    # print t2.name, Test.nis
    # print type(a),type(b),type(c)
    # print isinstance(a,list)
    # print d
    f=open('aaa.txt','w')
    f.write('hello \nworld\npython')
    print open('aaa.txt').read()
    os.remove('aaa.txt')

