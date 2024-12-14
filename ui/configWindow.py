import tkinter as tk
import ui.widgets as widgets

def check_if_file_exists(file):
    try:
        with open(f"./databases/{file}", "r") as f:
            return True
    except:
        return False

def get_configs():
    configPage = widgets.create_window(300, 700)
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

    widgets.create_label(configPage, "Databases sources (sqlite):", bg=widgets.Colors.WINDOW)
    frame = widgets.create_frame(configPage)
    frame.pack(pady=10)
    frame.configure(bg=widgets.Colors.WINDOW)

    sourcesEntries = []

    def add_source(default=""):
        entry = widgets.crete_entry(frame, default)
        deleteButton = widgets.create_button(frame, "Delete", lambda: delete_source(entry))

        entry.configure(width=20)
        deleteButton.configure(width=10)

        entry.pack()
        deleteButton.pack()
        
        sourcesEntries.append((entry, deleteButton))

    add_source("facebook.sqlite3")
    add_source("twitter.sqlite3")

    def delete_source(entry):
        for i, (e, b) in enumerate(sourcesEntries):
            if e == entry:
                e.destroy()
                b.destroy()
                sourcesEntries.pop(i)
                break

    addSourceButton = widgets.create_button(configPage, "Add source", add_source)
    addSourceButton.pack(pady=10)


    def on_confirm():
        numOfThreads = numOfThreadsEntry.get()
        fakeRequestDelay = fakeRequestDelayEntry.get()
        refreshDelay = refreshDelayEntry.get()
        numOfPosts = numOfPostsEntry.get()

        dbSources = []
        for entry, _ in sourcesEntries:
            dbSources.append(entry.get())

        if not dbSources:
            errorLabel.config(text="No sources added")
            return
        
        for source in dbSources:
            if not check_if_file_exists(source):
                errorLabel.config(text=f"File {source} does not exist")
                return

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
        data["sources"] =  dbSources

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
