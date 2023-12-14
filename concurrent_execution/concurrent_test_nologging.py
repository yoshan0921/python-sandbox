import multiprocessing
import threading
import asyncio
import time

WORK_MULTIPLICITY = 3
CPU_LOAD = 10**7
IO_LATENCY = 2
start = 0.0


def worker(n, start_time):
    """
    For synchronous, threading, multiprocessing
    """
    # cpu-bound
    for i in range(CPU_LOAD):
        pass

    # io-bound
    time.sleep(IO_LATENCY)

   # cpu-bound
    for i in range(CPU_LOAD):
        pass


def wrap_worker(args):
    """
    This is wrapper for worker() to separate arguments
    """
    return worker(*args)


async def worker_async(n, start_time):
    """
    For asyncio
    """
    # cpu-bound
    for i in range(CPU_LOAD):
        pass

    # io-bound
    await asyncio.sleep(IO_LATENCY)

    # cpu-bound
    for i in range(CPU_LOAD):
        pass

if __name__ == '__main__':
    # 1.synchronous
    for i in range(1, WORK_MULTIPLICITY+1):
        worker(i, start)

    # 2.asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        *[worker_async(i, start) for i in range(1, WORK_MULTIPLICITY+1)]))
    loop.close()

    # 3.threading
    for i in range(1, WORK_MULTIPLICITY+1):
        threading.Thread(target=worker, args=(i, start)).start()
    for thread in threading.enumerate():
        if thread is not threading.current_thread():
            thread.join()

    # 4.multiprocessing
    args = [(i, start) for i in range(1, WORK_MULTIPLICITY+1)]
    with multiprocessing.Pool(processes=WORK_MULTIPLICITY) as pool:
        pool.map(wrap_worker, args)
