import tkinter as tk
import ui.widgets as widgets

def get_configs():
    configPage = widgets.create_window(300, 400)
    configPage.title("Configuration")
    errorLabel = None

    data = {}

    widgets.create_label(configPage, "Number of threaded windows:", bg=widgets.Colors.WINDOW)
    numOfThreadsEntry = widgets.crete_entry(configPage, "5")

    widgets.create_label(configPage, "Fake request delay (sec):", bg=widgets.Colors.WINDOW)
    fakeRequestDelayEntry = widgets.crete_entry(configPage, "2")

    widgets.create_label(configPage, "Refresh every (sec):")
    refreshDelayEntry = widgets.crete_entry(configPage, "5")

    widgets.create_label(configPage, "Number of posts per thread:", bg=widgets.Colors.WINDOW)
    numOfPostsEntry = widgets.crete_entry(configPage, "5")

    def on_confirm():
        numOfThreads = numOfThreadsEntry.get()
        fakeRequestDelay = fakeRequestDelayEntry.get()
        refreshDelay = refreshDelayEntry.get()
        numOfPosts = numOfPostsEntry.get()

        if not numOfThreads or not numOfThreads.isdigit():
            errorLabel.config(text="Invalid number of threads")
            return
        
        if not fakeRequestDelay or not fakeRequestDelay.isdigit():
            errorLabel.config(text="Invalid delay")
            return
        
        if not refreshDelay or not refreshDelay.isdigit():
            errorLabel.config(text="Invalid refresh delay")
            return
        
        if not numOfPosts or not numOfPosts.isdigit():
            errorLabel.config(text="Invalid number of posts")
            return
        
        data["delay"] = int(fakeRequestDelay)
        data["refreshDelay"] = int(refreshDelay)
        data["numOfThreads"] = int(numOfThreads)
        data["numOfPosts"] = int(numOfPosts)

        configPage.quit()
        configPage.destroy()

    confirmButton = widgets.create_button(configPage, "Confirm", on_confirm)
    confirmButton.place(anchor="center")
    confirmButton.pack(pady=30)

    errorLabel = widgets.create_label(configPage, "", bg=widgets.Colors.WINDOW)
    errorLabel.configure(fg="red")
    errorLabel.pack()

    configPage.mainloop()

    if not data:
        exit()

    return data
