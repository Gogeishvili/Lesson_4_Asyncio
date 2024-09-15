import time

from async_Data_Loader import AsyncDataLoader
from data_Saver import DataSaver


def main():
    API = 'https://jsonplaceholder.typicode.com/posts/'
    start_time = time.time()

    data_loader = AsyncDataLoader()
    data_loader.load_data(API, 1, 78)

    data_saver = DataSaver()
    data_saver.save_data(data_loader.result)

    print(time.time() - start_time)


if __name__ == "__main__":
    main()
