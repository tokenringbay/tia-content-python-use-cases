import asyncio
import time

def fetch(url):
    """ Make the request and return the results """
    pass

def worker(name, queue, results):
    """
    A function to take unmake requests from the queue and perform the work,
    then add results to the results list
    """
    pass

async def distribute_work(url, requests, concurrency, results):
    """ Divide up the work into batches and collect the final results
    We need a queue, and we need a queue that will work assyncronosly """
    queue = asyncio.Queue()

    for _ in range(requests):
        queue.put_nowait(url)

    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        tasks.append(task)

    started_at = time.monotonic()
    """ Wait till every item in the queue is finished
    if it's not finished don't move to the next line """
    await queue.join()
    total_time = time.monotonic() - started_at

def assault(url, requests, concurrency):
    """ Entry point to making requests """
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)
    pass




