import threading

from ui.window import createWindow
from ui.widgets import createButton

from utils.ThreadFeed import register_refresh_feed
from utils.Storage import Storage


def button_callback():
    print("button clicked")


def onDataFetched(target):
    data = Storage.get(target)
    print(f"{target} data: {data}")


def onLoading(target, isLoading):
    print(f"{target} is loading: {isLoading}")


app = createWindow(300, 300)
button = createButton(app, "Click me", button_callback)


if __name__ == "__main__":
    targets = ["Twitter", "Facebook", "Instagram"]
    threads = [
        threading.Thread(
            target=register_refresh_feed, args=(target, onLoading, onDataFetched)
        )
        for target in targets
    ]
    for thread in threads:
        thread.start()

    app.mainloop()
