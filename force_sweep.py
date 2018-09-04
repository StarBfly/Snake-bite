class Class:
    def __del__(self):
        print(self.__class__.__name__, "deleted")


c1 = Class()
c2 = Class()

c1.ref = c2
c2.ref = c1

del c1, c2

import gc

gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.collect()

print(gc.garbage)
