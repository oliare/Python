# Decorators
# task 1
import time

def calcSec(func):
    def inner():
        begin = time.time()
        result = func()
        end = time.time()
        print(f"time: {end - begin} sec")
        return result
    return inner

@calcSec
def getEvenNumbers():
    return list(range(0, 1000, 2)) 

print(getEvenNumbers())


# 2
def replaceChar(func):
    def inner(*args):
        args_ = []
        for i in args:
            if isinstance(i, (int, float)) and i < 0:
                 args_.append(abs(i))
            else: args_.append(i)
        return func(*args_)
    return inner

@replaceChar
def func(*args): return args

print(func(-10, 'blabla', 77, -3, 12))

