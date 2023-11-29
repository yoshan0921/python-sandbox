import multiprocessing
import threading
import asyncio
import time
import logging

num_of_processings = 5

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s_%(threadName)s: %(message)s'
)


def io_bound():
    logging.debug(f"start")
    start = time.time()
    for i in range(10000):
        for j in range(10000):
            pass
    time.sleep(2)
    end = time.time()
    logging.debug(f"end -> time = {end - start}")


async def io_bound_async():
    logging.debug(f"start")
    start = time.time()
    for i in range(10000):
        for j in range(10000):
            pass
    await asyncio.sleep(2)
    end = time.time()
    logging.debug(f"end -> time = {end - start}")

if __name__ == '__main__':

    # single process single thread
    logging.debug(f"single process single thread: start")
    start = time.time()
    for i in range(num_of_processings):
        io_bound()
    end = time.time()
    logging.debug(
        f"single process single thread: end -> time = {end - start}\n")

    # threading
    logging.debug(f"threading: start")
    start = time.time()
    for i in range(num_of_processings):
        threading.Thread(target=io_bound).start()
    for thread in threading.enumerate():  # multiprocessing contains no analogues of threading.enumerate()
        if thread is not threading.current_thread():
            thread.join()
    end = time.time()
    logging.debug(f"threading: end -> time = {end - start}\n")

    # multiprocessing
    logging.debug(f"multiprocessing: start")
    start = time.time()
    process_list = []
    for i in range(num_of_processings):
        p = multiprocessing.Process(target=io_bound)
        process_list.append(p)
        p.start()
    for process in process_list:
        if process is not multiprocessing.current_process():
            process.join()
    end = time.time()
    logging.debug(f"multiprocessing: end -> time = {end - start}\n")

    # asyncio
    logging.debug(f"asyncio: start")
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        *[io_bound_async() for _ in range(num_of_processings)]))
    loop.close()
    end = time.time()
    logging.debug(f"asyncio: end -> time = {end - start}\n")
