import time

from utils.Fetcher import DataFetcher

def register_refresh_feed(source=None, onLoading=None, onFetch=None, delay=1, fake_request_delay=2, num_of_posts=5):

    while True:
        DataFetcher.fetch(source, onLoading, onFetch, fake_request_delay, num_of_posts)

        time.sleep(delay)
