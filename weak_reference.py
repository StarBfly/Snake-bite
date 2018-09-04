# garbage collector doesn't count weakref
# del method will work as usual


import weakref
class Class:
    def __del__(self):
        print(self.__class__.__name__, "deleted")

c1, c2 = Class(), Class()

c1.ref = weakref.ref(c2)
c2.ref = c1

del c1, c2
print("exit")
