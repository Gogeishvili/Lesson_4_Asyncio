import time
from async_Data_Loader import AsyncDataLoader


def main():
    API = 'https://jsonplaceholder.typicode.com/posts/'
    start_time = time.time()

    data_loader = AsyncDataLoader()
    data_loader.load_and_save_data(API, 1, 78)

    print(time.time() - start_time)


if __name__ == "__main__":
    main()
