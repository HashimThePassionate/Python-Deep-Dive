import asyncio

class AsyncLineReader:
    def __init__(self, lines):
        self.lines = lines
        self.index = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.index >= len(self.lines):
            raise StopAsyncIteration
        await asyncio.sleep(0.5)  # Simulate asynchronous I/O operation
        line = self.lines[self.index]
        self.index += 1
        return line

async def main():
    lines = [
        "🌟 Line 1: Hello, Async World!",
        "🚀 Line 2: Asyncio makes concurrency easy.",
        "🔍 Line 3: Iterators can be asynchronous."
    ]
    
    async for line in AsyncLineReader(lines):
        print(f"📄 Read: {line}")

asyncio.run(main())