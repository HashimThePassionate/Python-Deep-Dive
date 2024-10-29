import asyncio

async def fetch_data(source, delay):
    print(f"Fetching data from {source}")
    await asyncio.sleep(delay)  # Simulate I/O operation
    data = f"Data from {source}"
    print(f"Finished fetching from {source}")
    return data

async def main():
    # Schedule both fetch_data coroutines concurrently
    task1 = asyncio.create_task(fetch_data("Source 1", 2))
    task2 = asyncio.create_task(fetch_data("Source 2", 3))

    # Await both tasks to complete
    results = await asyncio.gather(task1, task2)

    print("Results:")
    for result in results:
        print(result)

asyncio.run(main())
