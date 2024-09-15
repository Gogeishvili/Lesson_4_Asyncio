
import aiohttp
import asyncio


class AsyncDataLoader:

    def __init__(self):
        self.__result = []
        self.__lock = asyncio.Lock()

    @property
    def result(self):
        return self.__result

    def load_data(self, base_api, start_id, end_id):
        asyncio.run(self.__load_data(base_api, start_id, end_id))

    async def __fetch_data(self, session, url):
        async with session.get(url, ssl=False) as response:
            result= await response.json()
            async with self.__lock:
                self.__result.append(result)

    async def __load_data(self, base_api, start_id, end_id):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(start_id, end_id):
                api = f"{base_api}{i}"
                tasks.append(self.__fetch_data(session, api))

            await asyncio.gather(*tasks)
