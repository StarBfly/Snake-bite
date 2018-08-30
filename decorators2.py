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

        def __getattribute__(self, name):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.cls_instance (an
            instance of the decorated class). If it manages to fetch the attribute from self.cls_instance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls, self).__getattribute__(name)
            except AttributeError:
                pass
            else:
                return x
            x = self.cls_instance.__getattribute__(name)
            if hasattr(x, "__call__"): # it is an instance method
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


def pause(t):
    def wrapper(f):
        def tmp(*args, **kwargs):
            print("Time stopping")
            time.sleep(t)
            print("Continue")
            return f(*args, **kwargs)
        return tmp

    return wrapper

@pause(4)
def func(x, y):
    return x + y

print(func(1, 2))


def Tracer(aClass): # On @ decorator
    class Wrapper:
        def __init__(self, *args, **kargs): # On instance creation
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs) # Use enclosing scope name

        def __getattr__(self, attrname):
            print('Trace: ' + attrname) # Catches all but own attrs
            self.fetches += 1
            return getattr(self.wrapped, attrname) # Delegate to wrapped obj
    return Wrapper
