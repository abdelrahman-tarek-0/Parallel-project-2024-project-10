import threading
import time

from utils.Fetcher import DataFetcher


def register_refresh_feed(target=None, onLoading=None, onFetch=None, delay=1):
    executer = None
    if target == "Twitter":
        executer = DataFetcher.fetch_from_twitter
    elif target == "Facebook":
        executer = DataFetcher.fetch_from_facebook
    elif target == "Instagram":
        executer = DataFetcher.fetch_from_instagram

    while True:
        print("\nRefreshing feed...")

        executer(onLoading, onFetch)

        time.sleep(delay)
