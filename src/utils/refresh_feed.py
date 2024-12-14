import time

from utils.Fetcher import DataFetcher


def register_refresh_feed(source=None, onLoading=None, onFetch=None, delay=1, fake_request_delay=2):

    while True:
        print("\nRefreshing feed...")

        DataFetcher.fetch(source, onLoading, onFetch, fake_request_delay)

        time.sleep(delay)
