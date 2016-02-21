class MySingleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton,self).__new__(self)
            self.x = 10
        return self._instance

x = MySingleton()
print x.x
x.x = 20
y = MySingleton()
print y.x
print x.x

def singleton(myClass):
    instances = {}
    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstance

@singleton
class Mark:
    def __init__(self):
        self.x = 15

x = Mark()
print x.x
x.x = 20
y = Mark()
print y.x
