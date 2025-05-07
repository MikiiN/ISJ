#!/usr/bin/env python3
import asyncio
import aiohttp


async def get_response(url):
    async with aiohttp.ClientSession() as session:
        try:
            response = await session.get(url)
            result = (response.status, url)
        except aiohttp.ClientConnectionError:
            result = ("aiohttpClientError", url)
    return result


async def get_urls(urls):
    tasks = []
    result = []
    for url in urls:
        tasks.append(asyncio.create_task(get_response(url)))
    for task in tasks:
        ret = await task
        result.append(ret)
    return result 

if __name__ == '__main__':
    urls = ['https://www.fit.vutbr.cz', 'https://www.szn.cz', 'https://www.alza.cz', 'https://office.com', 'https://aukro.cz']
    
    # for MS Windows
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    res = asyncio.run(get_urls(urls))
    print(res)