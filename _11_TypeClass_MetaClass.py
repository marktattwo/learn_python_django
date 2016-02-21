class MyClass(object):
	def __init__(self):
		self.x = 5

print dir()

x = MyClass()

print MyClass
print x
print type(x)
print MyClass == type(x)

def mark(self):
	print 'God Like'

TypeClass = type("TypeClass", (object,), {"x":5, "mark":mark})
#type(name, base classes, functions and vars)

y = TypeClass()

print x.x, y.x
y.mark()

print type("1")
print "1".__class__
print type(type("1"))
#type is a metaclass
#metaclass is type that create other type
#type same as __class__


class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class MyClass2(object):
	__metaclass__ = Singleton
	x = 10

x = MyClass2()
print 'x.x = ' + str(x.x)
x.x = 20
y = MyClass2()
print 'y.x = ' + str(y.x)