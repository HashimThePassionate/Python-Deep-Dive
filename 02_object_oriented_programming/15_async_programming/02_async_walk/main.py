import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def cpu_bound_task():
    # CPU-bound operation ko simulate karte hain
    sum(i * i for i in range(10 ** 7))
    print(f"{time.ctime()} CPU-bound task completed")

async def main():
    print(f"{time.ctime()} Main coroutine started")
    loop = asyncio.get_running_loop()

    # ProcessPoolExecutor create karna
    with ProcessPoolExecutor() as executor:
        await loop.run_in_executor(executor, cpu_bound_task)

    print(f"{time.ctime()} Main coroutine completed")

if __name__ == "__main__":
    # Event loop ko run karna
    asyncio.run(main())
