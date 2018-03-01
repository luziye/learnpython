import random
import re


def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'nowcoder')

    strb = ' \n\rhello nowcoder \r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()

    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 6, len(strc)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(' ')
    print 9, strc.find('ello')


def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 2, True, not True, False
    print 3, 1 < 2, 5 > 2
    print 4, 2 << 3


def demo_buildinfunction():
    print 1, max(2, 1), min(5, 3)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-2)
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x+3')
    print 7, chr(65), ord('a')
    print 8, divmod(11, 3)


def demo_condition():
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do special
            # print 'x'
        if i < 5:
            continue
        print i
        if i == 6:
            break


def demo_list():
    lista = [1, 2, 3]  # arraylist
    print 1, lista
    listb = ['a', 2, 'c', 3.3]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    listb.insert(0, 'www')
    print 6, listb
    listb.pop(1)
    print 7, listb
    listb.reverse()
    print 8, listb
    listb.sort(reverse=True)
    print 9, listb
    print 10, listb * 2

    tuplea = (1, 2, 3)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {1: 1, 2: 4, 3: 9}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1), dicta.has_key('3')
    for key, value in dicta.items():
        print 'key-value:', key, value
    dictb = {'+': add, '-': sub}
    print 4, dictb['+'](13, 2)
    print 5, dictb.get('-')(5, 2)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(2)
    print dicta
    del dicta[1]
    print dicta


def demo_set():
    seta = set((1, 2, 3))
    setb = set((2, 3, 4))
    print 1, seta
    # seta.add(4)
    # print 2,seta
    print 3, seta.intersection(setb), seta & setb
    print 4, seta.union(setb), seta | setb
    print 5, seta - setb
    seta.add('x')
    print 6, seta
    print 7, len(seta)


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'i am ' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'i am ' + self.name + ' ' + str(self.uid) + self.group


def demo_exception():
    try:
        # print 2/1
        print 2 / 1
        # if type=='c':
        raise Exception('raise error', 'nowcoder')
    except Exception as e:
        print 'error', e
    finally:
        print 'clean up'


def demo_random():
    # random.seed(1)
    print 1, int(random.random() * 100)
    print 2, random.randint(0, 200)
    print 3, random.choice(range(0, 100, 10))
    print 4, random.sample(range(0, 100), 4)
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print 5, a

def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print p1.findall(str)
    print p2.findall(str)

    str2 = 'qwiu@email.com;43@gmail.com;fei@gmail.com;reiy@qq.com'
    p3 = re.compile('[\w]+@[gmail|qq]+\.com')
    print p3.findall(str2)

    str3='<html><h>title</h><body>xxx</body></html>'
    p4=re.compile('<h>[^<]+</h>')
    print p4.findall(str3)
    p5=re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print p5.findall(str3)

    str4='xxx2018-03-01yyy'
    p6=re.compile('\d\d\d\d-\d\d-\d\d')
    p7=re.compile('\d{4}-\d{2}-\d{2}')
    # print p6.findall(str4)
    print p7.findall(str4)


if __name__ == '__main__':
    '''
    # user1=User('u1',1)
    # print user1
    # admin1=Admin('a1',101,' g1')
    # print admin1
    # print 'hello nowcoder'
    '''
    # comment
    demo_string()
    demo_operation()
    demo_buildinfunction()
    demo_condition()
    demo_list()
    demo_dict()
    demo_set()
    demo_exception()
    demo_random()
    demo_re()
