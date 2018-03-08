def is_ss(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def calc_sum(*args):
    ax=0
    for n in args:
        ax+=n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


def log(func):
    def wrapper(*args,**kargs):
        print 'call%s()'%func.__name__
        return func(*args,**kargs)
    return wrapper

def log(text):
    def decorator(func):
        def wrapper(*args, **kargs):
            print text,'call%s()' % func.__name__
            return func(*args, **kargs)
        return wrapper
    return decorator

@log('lzy')
def now():
    print '2018-3-8'


if __name__=='__main__':
    # print is_ss(29)
    # print filter(is_ss,[x for x in range(1,101)])
    # f=lazy_sum(1,3,5,7,9)
    # print f()
    now()