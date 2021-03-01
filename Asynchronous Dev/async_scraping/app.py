import asyncio
import aiohttp
import async_timeout
import time
import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

# Page 1
page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

loop = asyncio.get_event_loop()

books = page.books

async def fetch_page(session, url):
    async with async_timeout.timeout(10):
        start = time.time()
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)

urls = [f'https://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(0, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f"Total page requests took {time.time() - start}")

for page_content in pages:
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)

# # Start by page 2
# for page_num in range(1, page.page_count):
#     url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
#     page_content = requests.get(url).content
#     logger.debug('Creating AllBooksPage from page content.')
#     page = AllBooksPage(page_content)
#     books.extend(page.books)
