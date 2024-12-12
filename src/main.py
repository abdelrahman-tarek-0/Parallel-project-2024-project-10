import threading
from random import randint

from ui.multiWindows import CreateWindow
from ui.multiWindows import start

import ui.widgets as widgets


from utils.refresh_feed import register_refresh_feed
from utils.Storage import InMemorySharedStorage

facebookWindow = CreateWindow(x=50, y=50, width=800, height=400)
facebookWindow.w.title("Facebook")

twitterWindow = CreateWindow(x=100, y=50, width=800, height=400)
twitterWindow.w.title("Twitter")

instagramWindow = CreateWindow(x=150, y=50, width=800, height=400)
instagramWindow.w.title("Instagram")

# app = createWindow(800, 800)
frames = {
    "Twitter": {
        "frame": widgets.create_data_frame(twitterWindow.w),
        "window": twitterWindow,
        "labels": [],
        "loading_label": None,
    },
    "Facebook": {
        "frame": widgets.create_data_frame(facebookWindow.w),
        "window": facebookWindow,
        "labels": [],
        "loading_label": None,
    },
    "Instagram": {
        "frame": widgets.create_data_frame(instagramWindow.w),
        "window": instagramWindow,
        "labels": [],
        "loading_label": None,
    },
}

def onDataFetched(target):
    data = InMemorySharedStorage.get(target)
    print(f"{target} data: {data}")

    frame = frames[target]
    for label in frame["labels"]:
        label.destroy()

    for i, post in enumerate(data):
        print(f"{i + 1}. {post}")
        label = widgets.create_label(frame["frame"], f"{i + 1}. {post}")
        frame["labels"].append(label)

def onLoading(target, isLoading):
    frame = frames[target]
    if isLoading:
        if frame["loading_label"] is None:
            frame["loading_label"] = widgets.create_label(frame["frame"], "Loading...")

        for label in frame["labels"]:
            label.destroy()

    else:
        if frame["loading_label"] is not None:
            frame["loading_label"].destroy()
            frame["loading_label"] = None


if __name__ == "__main__":
    targets = ["Twitter", "Facebook", "Instagram"]

    threads = [
        threading.Thread(
            target=register_refresh_feed, args=(target, onLoading, onDataFetched, randint(1, 3))
        )
        for target in targets
    ]
    for thread in threads:
        thread.start()

    start()
