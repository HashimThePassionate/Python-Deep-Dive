import asyncio
import aiohttp

async def download_file(session, url):
    print(f"Starting download from {url}")
    async with session.get(url) as response:
        content = await response.read()
        filename = url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(content)
    print(f"Finished downloading {filename}")

async def main():
    urls = [
        'https://www.example.com/file1.txt',
        'https://www.example.com/file2.txt',
        'https://www.example.com/file3.txt',
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())
