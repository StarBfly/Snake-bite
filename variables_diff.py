a = 1


#returns local var
def foo():
    a = 2
    return a


print(foo())

#return local global
def foo5():
    return a


print(foo5())


#overrides global var
def foo1(a):
    a = 2
    return a


print(foo1(a))

#all possible


def foo2():
    #print(a) #will not print 1...
    a = 3
    def foo3():
        a = 4
        return a
    return foo3()

print(foo2())
