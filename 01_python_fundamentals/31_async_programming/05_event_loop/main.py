import asyncio

def get_loop():
    loop = asyncio.get_event_loop()
    print(f"Event loop: {loop}")

get_loop()
