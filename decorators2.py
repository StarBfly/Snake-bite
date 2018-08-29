#Decoratora with arguments
import datetime
import time

a = 1

b = 2


def arguments_wrapper(arg1, arg2):
    def real_wrapper(some_func):
        def _wrapper(*args, **kwargs):
            print(f"Arguments {arg1} and {arg2} were given")
            print(some_func(*args, **kwargs))
            print(f"Arguments {arg1} and {arg2} were processed")
        return _wrapper
    return real_wrapper


@arguments_wrapper(a, b)
def func(num1, num2):
    return num1 + num2

func(a, b)


#simple decorator
def time_this(original_function):
    print("Fucntion is decorated with time")
    def wrapper(*args,**kwargs):
        print("Timer started")
        before = datetime.datetime.now()
        original_function(*args,**kwargs)
        after = datetime.datetime.now()
        print(f"Elapsed Time = {after-before}")
    return wrapper

@time_this
def simp_func():
    for i in range(10):
        print(i)
        time.sleep(2)


#class decorator
def time_all_class_methods(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self.cls_instance = cls(*args, **kwargs)

        def __getattribute__(self, s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.cls_instance.__getattribute__(s)
            if type(x) == type(self.__init__): # it is an instance method
                return time_this(x)                 # this is equivalent of just decorating the method with time_this
            else:
                return x
    return NewCls


#simple class to test decorator
@time_all_class_methods
class Foo:

    def a(self):
        print("entering a-method")
        import time
        time.sleep(3)
        print("exiting a-method")


foo_object = Foo()
foo_object.a()