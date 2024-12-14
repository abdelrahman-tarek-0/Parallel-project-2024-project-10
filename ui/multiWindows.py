import tkinter as tk

import threading
import time

from ui.widgets import Colors
root = tk.Tk()
root.withdraw()


class CreateWindow:
    open_windows = 0

    def build(self, x=50, y=50, width=250, height=100):
        self.w = tk.Toplevel()

        self.w.title("Threaded Window")
        self.w.configure(bg=Colors.WINDOW)
        self.w.grid_columnconfigure(0, weight=1)
        self.w.grid_columnconfigure(1, weight=1)

        self.w.geometry(
            f"{width}x{height}+{int(round(width/100*x))}+{int(round(height/100*y))}"
        )

        self.w.protocol("WM_DELETE_WINDOW", self.on_close)
        self.w.update()
        time.sleep(0.2)

    def on_close(self):
        self.w.destroy()
        CreateWindow.open_windows -= 1

        if CreateWindow.open_windows <= 0:
            root.destroy()

    def __init__(self, x=50, y=50, width=250, height=100):
        CreateWindow.open_windows += 1
        thread = threading.Thread(
            target=self.build(x, y, width, height), daemon=True
        )
        thread.start()
        time.sleep(0.2)


def start():
    root.mainloop()