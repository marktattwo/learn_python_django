BaseClass = type("BaseClass", (object,), {})
C1 = type('C1', (BaseClass,), {'x':1})
C2 = type('C2', (BaseClass,), {'x':2})

def MyFactory(myBool):
	return C1() if myBool else C2()

m = MyFactory(True)
n = MyFactory(False)
print m.x, n.x

###################################################

class MyClass:
	#no need to create instance
	@classmethod
	def mark(self):
		print 'Awesome!'

MyClass.mark()

##################################################
BaseClass2 = type("BaseClass2", (object,), {})

@classmethod
def Check1(self, choice):
	return choice == '1'

@classmethod
def Check2(self, choice):
	return choice == '2'

Cl1 = type('Cl1', (BaseClass2,), {'x':10, 'Check':Check1})
Cl2 = type('Cl2', (BaseClass2,), {'x':20, 'Check':Check2})

def MyFactory2(choice):
	for cls in BaseClass2.__subclasses__():
		if cls.Check(choice):
			return cls()

a = MyFactory2('1')
b = MyFactory2('2')

print a.x, b.x