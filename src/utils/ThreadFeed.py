import threading
import time
from random import randint

from utils.Storage import Storage


# Mock APIs
def fetch_from_twitter():
    time.sleep(2)
    random = randint(0, 100000)
    return Storage.save(
        "Twitter",
        ["Twitter Post 1", "Twitter Post 2", "Twitter Post 3", f"Random: {random}"],
    )


def fetch_from_facebook():
    time.sleep(2)
    random = randint(0, 100000)
    return Storage.save(
        "Facebook",
        ["Facebook Post 1", "Facebook Post 2", "Facebook Post 3", f"Random: {random}"],
    )


def fetch_from_instagram():
    time.sleep(2)
    random = randint(0, 100000)
    return Storage.save(
        "Instagram",
        [
            "Instagram Post 1",
            "Instagram Post 2",
            "Instagram Post 3",
            f"Random: {random}",
        ],
    )


def register_refresh_feed(target=None, onLoading=None, onFetch=None, delay=1):
    executer = (
        fetch_from_twitter
        if target == "Twitter"
        else (
            fetch_from_facebook
            if target == "Facebook"
            else fetch_from_instagram if target == "Instagram" else None
        )
    )

    while True:
        print("\nRefreshing feed...")

        threads = [threading.Thread(target=executer, args=())]

        if onLoading:
            onLoading(target, True)

        # Start and join threads
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        if onLoading:
            onLoading(target, False)

        if onFetch:
            onFetch(target)

        time.sleep(delay)
