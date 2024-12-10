import customtkinter


def createButton(app, text, command):
    button = customtkinter.CTkButton(app, text=text, command=command)
    button.pack(padx=20, pady=20)
    return button
