import threading
import logging

from ui.multiWindows import CreateWindow
from ui.multiWindows import start
from ui.configWindow import get_configs

import ui.widgets as widgets

from utils.refresh_feed import register_refresh_feed
from utils.Storage import InMemorySharedStorage

configs = get_configs()

frames = {}


for i in range(configs["numOfThreads"]):
    window = CreateWindow(x=i * 50, y=50, width=600, height=600)

    window.w.title(f"Threaded Window {i + 1}")
    frames[f"frame_{i}"] = {
        "frame": widgets.create_data_frame(window.w),
        "window": window,
        "loading_label": None,
    }


def onDataFetched(target):
    try:
        data = InMemorySharedStorage.get(target)
        frame = frames[target]

        for widget in frame["frame"].winfo_children():
            widget.destroy()

        for post in data:
            widgets.create_user_post(frame["frame"], post)

    except Exception:
        logging.warning(f"Target: {target} - probably closed window (ignoring)")


def onLoading(target, isLoading):
    try:
        frame = frames[target]
        if isLoading:
            for widget in frame["frame"].winfo_children():
                widget.destroy()

            if frame["loading_label"] is None:
                frame["loading_label"] = widgets.create_label(frame["frame"], "Loading...")

        else:
            if frame["loading_label"] is not None:
                frame["loading_label"].destroy()
                frame["loading_label"] = None
    except Exception:
        logging.warning(f"Target: {target} - probably closed window (ignoring)")

if __name__ == "__main__":
    targets = list(frames.keys())
    
    delay = configs["refreshDelay"]
    fake_request_delay = configs["delay"]
    number_of_posts = configs["numOfPosts"]
    is_multi_threading = configs["multiThreading"]

    threads = [
        threading.Thread(
            target=register_refresh_feed,
            args=(
                target,
                configs["sources"],
                onLoading,
                onDataFetched,
                delay,
                fake_request_delay,
                number_of_posts,
                is_multi_threading,
            ),
        )
        for target in targets
    ]
    for thread in threads:
        thread.start()

    start()
