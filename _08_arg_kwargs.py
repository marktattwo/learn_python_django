def MyFunc(a,*args):
    for arg in args:
        print arg

l=['q','w','e','r','t','y']
MyFunc(1,2,3,4,*l)


def MyFunc2(a=123,b=5345):
    print a,b

MyFunc2()
MyFunc2(b=3)

def MyFunc3(**kwargs):
    for item in kwargs.items():
        print item
    for item in kwargs:
        print item
        print kwargs[item]

MyFunc3(x = 5, y = 10)

def MyFunc4(*args,**kwargs):
    for item in kwargs.items():
        print item
    for arg in args:
        print arg

MyFunc4(1,2,3,x=5)
