class BaseClass(object):
    def test(self):
        print 'hello'

class MyClass1(BaseClass):
    pass

class MyClass2(BaseClass):
    def test(self):
        print 'hi'

x = BaseClass()
x.test()
y = MyClass1()
y.test()
z = MyClass2()
z.test()
print BaseClass.__subclasses__()
