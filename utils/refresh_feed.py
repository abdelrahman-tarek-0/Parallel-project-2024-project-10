import time
import threading
import random

from utils.Fetcher import DataFetcher
from utils.Storage import InMemorySharedStorage


def register_refresh_feed(
    source=None,
    dbs=[],
    onLoading=None,
    onFetch=None,
    delay=1,
    fake_request_delay=2,
    num_of_posts=5,
):

    list_number_of_posts = [num_of_posts // len(dbs) for _ in range(len(dbs))]

    for i in range(num_of_posts % len(dbs)):
        list_number_of_posts[i] += 1

    while True:
        timeStart = time.time()
        onLoading(source, True)

        data = []
        threads = []

        for i, db in enumerate(dbs):
            t = threading.Thread(
                target=lambda db, fake_request_delay, num_of_posts: data.extend(
                    DataFetcher.fetch(db, fake_request_delay, num_of_posts)
                ),
                args=(
                    db,
                    fake_request_delay,
                    list_number_of_posts[i],
                ),
            )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        timeEnd = time.time()
        print(f"Fetching data for {source} took {timeEnd - timeStart} seconds")

        random.shuffle(data)

        InMemorySharedStorage.save(source, data)

        onLoading(source, False)
        onFetch(source)

        time.sleep(delay)
