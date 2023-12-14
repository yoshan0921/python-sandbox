from contextlib import contextmanager


@contextmanager
def context_manager_func():
    print('__enter__')
    try:
        yield "test"
    # except Exception as e:
    #     print("Exception is caught")
    finally:
        # Always done last, whether an exception occurs or not.
        print('__exit__')


if __name__ == '__main__':
    try:
        with context_manager_func() as cm:
            print("start work")
            raise Exception("")
            print("end work")
    except Exception as e:
        print("Exception is propagated to caller")
