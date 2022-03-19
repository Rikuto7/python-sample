import asyncio

import aiohttp


def main():
    asyncio.run(create_tasks())


async def create_tasks():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(session)
        ]

        result = await asyncio.gather(*tasks)
        return result


async def task_function(session):
    url = ""
    headers = {"Authorization": f"Bearer token"}
    async with session.get(url, headers=headers) as response:
            data = await response.json()
    return data
