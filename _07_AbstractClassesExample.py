from abc import ABCMeta, abstractmethod

class BaseClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def hello(self):
        pass
    
    #@abstractmethod
    def goodBye(self):
        pass

class InClass(BaseClass):
    def hello(self):
        print 'hello'

x = InClass()
x.goodBye()
