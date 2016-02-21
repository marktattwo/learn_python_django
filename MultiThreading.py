import threading
def printOne():
	for x in xrange(40):
		print 'a'

def printTwo():
	for x in xrange(40):
		print 'b'



# printOne()
if __name__ == '__main__':

	threadList = []

	###############################################################

	t1 = threading.Thread(target = printOne, args = ())
	t2 = threading.Thread(target = printTwo, args = ())

	threadList.append(t1)
	threadList.append(t2)

	t1.start()
	t2.start()

	print threading.activeCount()

	###############################################################
	
	