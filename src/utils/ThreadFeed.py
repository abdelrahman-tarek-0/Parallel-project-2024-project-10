import threading
import time

from utils.Fetcher import Fetcher
from utils.Storage import Storage


def register_refresh_feed(target=None, onLoading=None, onFetch=None, delay=1):
    executer = None
    if target == "Twitter":
        executer = Fetcher.fetch_from_twitter
    elif target == "Facebook":
        executer = Fetcher.fetch_from_facebook
    elif target == "Instagram":
        executer = Fetcher.fetch_from_instagram

    while True:
        print("\nRefreshing feed...")
        if Storage.get("kill") == True:
            return

        threads = [threading.Thread(target=executer, args=(onLoading, onFetch))]

        # Start and join threads
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        time.sleep(delay)
