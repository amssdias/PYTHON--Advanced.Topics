import aiohttp
import asyncio
import time

async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            print(f"Page took {time.time() - page_start}")
            return response.status

loop = asyncio.get_event_loop()

# We are getting coroutines objects, we not calling the function!!!
# No requests are being made, only coroutines are being made
tasks = [fetch_page('http://google.com') for i in range(50)]

start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f"All took {time.time() - start}")