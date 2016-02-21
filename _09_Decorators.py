def addOne(x):
    def addOneInside():
        return x() + 1
    return addOneInside

@addOne
def oldFunc():
    return 3

print oldFunc()
