import aiohttp
import asyncio
from data_Saver import DataSaver


class AsyncDataLoader:
    def __init__(self):
        self.__result = []
        self.__lock = asyncio.Lock()

    def load_and_save_data(self, base_api, start_id, end_id):
        asyncio.run(self.__load_and_save_data(base_api, start_id, end_id))

    async def __load_and_save_data(self, base_api, start_id, end_id):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(start_id, end_id):
                api = f"{base_api}{i}"
                tasks.append(self.__fetch_data(session, api))
            await asyncio.gather(*tasks)

    async def __fetch_data(self, session, url):
        async with session.get(url, ssl=False) as response:
            result = await response.json()
            async with self.__lock:
                self.__result.append(result)
                DataSaver.save_data(self.__result)
