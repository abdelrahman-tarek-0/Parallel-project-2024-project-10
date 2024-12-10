import threading
import customtkinter

from ui.window import createWindow
import ui.widgets as widgets

from utils.ThreadFeed import register_refresh_feed
from utils.Storage import Storage


app = createWindow(800, 800)
frames = {
    "Twitter": {
        "frame": widgets.create_data_frame(app, "Twitter", 0, 0),
        "labels": [],
        "loading_label": None,
    },
    "Facebook": {
        "frame": widgets.create_data_frame(app, "Facebook", 0, 1),
        "labels": [],
        "loading_label": None,
    },
    "Instagram": {
        "frame": widgets.create_data_frame(app, "Instagram", 1, 0, 2),
        "labels": [],
        "loading_label": None,
    },
}


def onDataFetched(target):
    data = Storage.get(target)
    print(f"{target} data: {data}")

    frame = frames[target]
    for label in frame["labels"]:
        label.destroy()

    for i, post in enumerate(data):
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
            target=register_refresh_feed, args=(target, onLoading, onDataFetched, 5)
        )
        for target in targets
    ]
    for thread in threads:
        thread.start()

    app.mainloop()
    Storage.save("kill", True)
    exit()
