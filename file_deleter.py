# method __del__ will be launched automatically
# GarbageCollector is not responsible for this
# after the program was run and all object refs don't exist anymore - all objects will be deleted
# to free the memory


class Class1:
    def __del__(self):
        print(self.__class__.__name__, "deleted")


class Class2:
    def __del__(self):
        print(self.__class__.__name__, "deleted")


a = Class1()
b = Class2()
print("exit")
