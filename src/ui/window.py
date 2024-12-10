import customtkinter

def createWindow(width, height):
    app = customtkinter.CTk()
    app.geometry(f"{width}x{height}")

    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    return app
