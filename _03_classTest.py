class Mark:
    '''
    Love U
    '''
    y = 5
    def __init__(self):
        self.x = 0
    def add(self,a):
        Mark.y += a        
i = Mark()
i.add(5)
j = Mark()
j.y = 100
j.add(10)

print i.y
print j.y
print Mark.y
print vars(i)
print vars(j)
print vars(Mark)
print i.__doc__
