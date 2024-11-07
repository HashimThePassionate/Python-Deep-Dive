import asyncio

class AsyncConnection:
    async def __aenter__(self):
        print("🔗 Opening connection...")
        await asyncio.sleep(1)  # Simulate asynchronous setup
        self.connection = "Connected"
        print("🔗 Connection opened.")
        return self.connection  # Resource to be used within the block
    
    async def __aexit__(self, exc_type, exc, tb):
        print("🔗 Closing connection...")
        await asyncio.sleep(1)  # Simulate asynchronous teardown
        self.connection = None
        print("🔗 Connection closed.")

async def main():
    async with AsyncConnection() as conn:
        print(f"💬 Using connection: {conn}")
        await asyncio.sleep(2)  # Simulate using the connection

asyncio.run(main())