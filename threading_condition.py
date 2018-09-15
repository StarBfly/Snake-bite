import threading


def odd_numbers_generator():
    for odd in range(1, 101, 2):
        yield odd


def even_numbers_generator():
    for even in range(2, 101, 2):
        yield even


FIRST_ODD_PRINTED = False


class CountingThread(threading.Thread):
    def __init__(self, num_type, cv):
        super(CountingThread, self).__init__()
        self.num_type = num_type
        self.cv = cv

    def run(self):
        if self.num_type == "odd":
            for i in odd_numbers_generator():
                with self.cv:
                    print(f"Odd thread number: {i}")
                    global FIRST_ODD_PRINTED
                    FIRST_ODD_PRINTED = True
                    self.cv.notify()
                    self.cv.wait()

        else:
            for i in even_numbers_generator():
                with self.cv:
                    while not FIRST_ODD_PRINTED:
                        self.cv.wait()
                    print(f"Even thread number: {i}")
                    self.cv.notify()
                    self.cv.wait()


cv = threading.Condition()

odd_thread = CountingThread(num_type="odd",
                            cv=cv)

even_thread = CountingThread(num_type="even",
                             cv=cv)

odd_thread.start()

even_thread.start()


odd_thread.join()
even_thread.join()
