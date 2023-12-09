import multiprocessing
import threading
import asyncio
import time
import logging

WORK_MULTIPLICITY = 3
CPU_LOAD = 10**8
IO_LATENCY = 2
start = 0.0

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s_%(threadName)s: %(message)s'
)


def worker(n, start_time):
    logging.debug(f"worker_{n}: start")
    logging.debug(f"worker_{n}: checkpoint1 = {
                  time.time() - start_time:06.3f}")

    # cpu-bound
    for i in range(CPU_LOAD):
        # check progress
        if i == CPU_LOAD//4*1:
            logging.debug(
                f"worker_{n}: checkpoint1-1 = {time.time() - start_time:06.3f}")
        elif i == CPU_LOAD//4*2:
            logging.debug(
                f"worker_{n}: checkpoint1-2 = {time.time() - start_time:06.3f}")
        elif i == CPU_LOAD//4*3:
            logging.debug(
                f"worker_{n}: checkpoint1-3 = {time.time() - start_time:06.3f}")

    logging.debug(f"worker_{n}: checkpoint2 = {
                  time.time() - start_time:06.3f}")

    # io-bound
    """
    The I/O bounds should actually be verified using such as the following libraries, but this time, I will simplify that part by replacing with time.sleep() as an example.
 	- File I/O -> files -> built-in modules/functions
	- Network I/O (HTTP) -> requests
	- Network I/O (DB) -> sqlite
    """
    time.sleep(IO_LATENCY)

    logging.debug(f"worker_{n}: checkpoint3 = {
                  time.time() - start_time:06.3f}")

   # cpu-bound
    for i in range(CPU_LOAD):
        pass

    logging.debug(f"worker_{n}: checkpoint4 = {
                  time.time() - start_time:06.3f}")
    logging.debug(f"worker_{n}: end")

# This is wrapper for worker() to separate arguments


def wrap_worker(args):
    return worker(*args)


async def worker_async(n, start_time):
    logging.debug(f"worker_{n}: start")
    logging.debug(f"worker_{n}: checkpoint1 = {
                  time.time() - start_time:06.3f}")

    # cpu-bound
    for i in range(CPU_LOAD):
        # check progress
        if i == CPU_LOAD//4*1:
            logging.debug(
                f"worker_{n}: checkpoint1-1 = {time.time() - start_time:06.3f}")
        elif i == CPU_LOAD//4*2:
            logging.debug(
                f"worker_{n}: checkpoint1-2 = {time.time() - start_time:06.3f}")
        elif i == CPU_LOAD//4*3:
            logging.debug(
                f"worker_{n}: checkpoint1-3 = {time.time() - start_time:06.3f}")

    logging.debug(f"worker_{n}: checkpoint2 = {
                  time.time() - start_time:06.3f}")

    # io-bound
    """
    The I/O bounds should actually be verified using such as the following libraries, but this time, I will simplify that part by replacing with asyncio.sleep() as an example.
	- File I/O -> aiofiles
	- Network I/O (HTTP) -> aiohttp 
	- Network I/O (DB) -> aiosqlite
    """
    await asyncio.sleep(IO_LATENCY)

    logging.debug(f"worker_{n}: checkpoint3 = {
                  time.time() - start_time:06.3f}")

    # cpu-bound
    for i in range(CPU_LOAD):
        pass

    logging.debug(f"worker_{n}: checkpoint4 = {
                  time.time() - start_time:06.3f}")
    logging.debug(f"worker_{n}: end")

if __name__ == '__main__':
    # 1.synchronous
    logging.debug(f"synchronous: start")
    start = time.time()

    for i in range(WORK_MULTIPLICITY):
        worker(i, start)

    end_1 = time.time() - start
    logging.debug(f"synchronous: end = {end_1:06.3f}\n")

    # 2.asyncio
    logging.debug(f"asyncio: start")
    start = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        *[worker_async(i, start) for i in range(WORK_MULTIPLICITY)]))
    loop.close()

    end_2 = time.time() - start
    logging.debug(f"asyncio: end = {end_2:06.3f}\n")

    # 3.threading
    logging.debug(f"threading: start")
    start = time.time()

    for i in range(WORK_MULTIPLICITY):
        threading.Thread(target=worker, args=(i, start)).start()
    for thread in threading.enumerate():
        if thread is not threading.current_thread():
            thread.join()

    end_3 = time.time() - start
    logging.debug(f"threading: end = {end_3:06.3f}\n")

    # 4.multiprocessing
    logging.debug(f"multiprocessing: start")
    start = time.time()

    args = [(i, start) for i in range(WORK_MULTIPLICITY)]
    with multiprocessing.Pool(processes=WORK_MULTIPLICITY) as pool:
        pool.map(wrap_worker, args)

    end_4 = time.time() - start
    logging.debug(f"multiprocessing: end = {end_4:06.3f}\n")

    # Result
    print("Result:")
    print(f"1.synchronous       : {end_1:06.3f} seconds")
    print(f"2.asyncio           : {end_2:06.3f} seconds")
    print(f"3.threading         : {end_3:06.3f} seconds")
    print(f"4.multiprocessing   : {end_4:06.3f} seconds")
