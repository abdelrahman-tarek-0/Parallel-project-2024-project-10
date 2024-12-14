import threading
import time

from utils.Fetcher import DataFetcher


def register_refresh_feed(source=None, onLoading=None, onFetch=None, delay=1):

    while True:
        print("\nRefreshing feed...")

        DataFetcher.fetch(source, onLoading, onFetch)

        time.sleep(delay)
