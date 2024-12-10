import time
from random import randint

from utils.Storage import Storage


class Fetcher:
    @staticmethod
    def _fetch(source, onLoading, onFetched):
        onLoading(source, True)
        time.sleep(2)
        random = randint(0, 100000)
        Storage.save(
            source,
            [f"{source} Post 1", f"{source} Post 2", f"{source} Post 3", f"Random: {random}"],
        )
        onLoading(source, False)
        onFetched(source)

    @staticmethod
    def fetch_from_twitter(onLoading, onFetched):
        Fetcher._fetch("Twitter", onLoading, onFetched)

    @staticmethod
    def fetch_from_facebook(onLoading, onFetched):
        Fetcher._fetch("Facebook", onLoading, onFetched)

    @staticmethod
    def fetch_from_instagram(onLoading, onFetched):
        Fetcher._fetch("Instagram", onLoading, onFetched)
