class ContextManager(object):

    def __init__(self):
        print("call __init__")

    def __enter__(self):
        print("call __enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("call __exit__")
        if exc_type is None:
            print('exit normally')
        else:
            print(f'exc_type={exc_type}')
            return True  # Propagate the exception

    def work(self):
        print("start work")
        # raise Exception()  # Exception occurred
        print("end work")


if __name__ == '__main__':
    try:
        with ContextManager() as cm:
            cm.work()
    except Exception as e:
        print("Exception is propagated to the caller")
