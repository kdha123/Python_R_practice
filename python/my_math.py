def absolute(n):
    r = 0
    if n < 0:
       r = n * -1
    else:
        r = n
    return r

def f(x):
    result = (2 * x) + 1
    return result

def fac(x):
    result = 1
    for h in range(1,x+1):
        result = result * h
    return result

def plus_minus(x, y):
    return [x + y, x - y]

def gubun():
    print('==============================================================')
