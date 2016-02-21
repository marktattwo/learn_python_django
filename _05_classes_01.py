class Mark(object):
    def __init__(self):
        self.x = 5
    def __hello(self):
        print 'Hello'
    def hello(self):
        self.__hello()


class Mark2(Mark):
    def __init__(self):
        super(Mark2, self).__init__()

x = Mark()
x.hello()
print x.x
