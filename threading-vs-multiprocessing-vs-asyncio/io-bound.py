import multiprocessing
import random
import threading
import asyncio
import time
import logging

CPU_LOAD = 10**4
PROCESSING_MULTIPLICITY = 3

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s_%(threadName)s: %(message)s'
)


def io_bound():
    logging.debug(f"start")
    start = time.time()

    # cpu bound task
    for i in range(CPU_LOAD):
        for j in range(CPU_LOAD):
            pass
    end_1 = time.time()
    logging.debug(f"end_1 -> time = {end_1 - start}")

    # io bound task
    time.sleep(2)

    end_2 = time.time()
    logging.debug(f"end_2 -> time = {end_2 - start}")


async def io_bound_async():
    logging.debug(f"start")
    start = time.time()

    # cpu bound task
    for i in range(CPU_LOAD):
        for j in range(CPU_LOAD):
            pass

    end_1 = time.time()
    logging.debug(f"end_1 -> time = {end_1 - start}")

    # io bound task
    await asyncio.sleep(2)

    end_2 = time.time()
    logging.debug(f"end_2 -> time = {end_2 - start}")

if __name__ == '__main__':

    # 1.sequential
    logging.debug(f"sequential: start")
    start_1 = time.time()
    for i in range(PROCESSING_MULTIPLICITY):
        io_bound()

    end_1 = time.time()
    logging.debug(f"sequential: end -> time = {end_1 - start_1}\n")

    # 2.asyncio
    logging.debug(f"asyncio: start")
    start_2 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        *[io_bound_async() for _ in range(PROCESSING_MULTIPLICITY)]))
    loop.close()
    end_2 = time.time()
    logging.debug(f"asyncio: end -> time = {end_2 - start_2}\n")

    # 3.threading
    logging.debug(f"threading: start")
    start_3 = time.time()
    for i in range(PROCESSING_MULTIPLICITY):
        threading.Thread(target=io_bound).start()
    for thread in threading.enumerate():
        if thread is not threading.current_thread():
            thread.join()
    end_3 = time.time()
    logging.debug(f"threading: end -> time = {end_3 - start_3}\n")

    # 4.multiprocessing
    logging.debug(f"multiprocessing: start")
    start_4 = time.time()
    process_list = []
    for i in range(PROCESSING_MULTIPLICITY):
        p = multiprocessing.Process(target=io_bound)
        process_list.append(p)
        p.start()
    for process in process_list:
        if process is not multiprocessing.current_process():
            process.join()
    end_4 = time.time()
    logging.debug(f"multiprocessing: end -> time = {end_4 - start_4}\n")

    # Result
    print("Result:")
    print(f"1.sequential        : {end_1 - start_1:0.2f}(s)")
    print(f"2.asyncio           : {end_2 - start_2:0.2f}(s)")
    print(f"3.threading         : {end_3 - start_3:0.2f}(s)")
    print(f"4.multiprocessing   : {end_4 - start_4:0.2f}(s)")
