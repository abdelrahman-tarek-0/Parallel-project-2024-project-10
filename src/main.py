import threading
from random import randint

from ui.multiWindows import CreateWindow
from ui.multiWindows import start

import ui.widgets as widgets

from utils.refresh_feed import register_refresh_feed
from utils.Storage import InMemorySharedStorage

facebookWindow = CreateWindow(x=0, y=50, width=600, height=600)
facebookWindow.w.title("Facebook")

twitterWindow = CreateWindow(x=50, y=50, width=600, height=600)
twitterWindow.w.title("Twitter")

instagramWindow = CreateWindow(x=100, y=50, width=600, height=600)
instagramWindow.w.title("Instagram")


frames = {
    "Twitter": {
        "frame": widgets.create_data_frame(twitterWindow.w),
        "window": twitterWindow,
        "loading_label": None,
    },
    "Facebook": {
        "frame": widgets.create_data_frame(facebookWindow.w),
        "window": facebookWindow,
        "loading_label": None,
    },
    "Instagram": {
        "frame": widgets.create_data_frame(instagramWindow.w),
        "window": instagramWindow,
        "loading_label": None,
    },
}

def onDataFetched(target):
    data = InMemorySharedStorage.get(target)
    frame = frames[target]

    for widget in frame["frame"].winfo_children():
        widget.destroy()

    for post in data:
        widgets.create_user_post(frame["frame"], post)

def onLoading(target, isLoading):
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


if __name__ == "__main__":
    targets = ["Twitter", "Facebook", "Instagram"]
    delay = 5 #randint(1, 3)
    threads = [
        threading.Thread(
            target=register_refresh_feed, args=(target, onLoading, onDataFetched,delay )
        )
        for target in targets
    ]
    for thread in threads:
        thread.start()

    start()
