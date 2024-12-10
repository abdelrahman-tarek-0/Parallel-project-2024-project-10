import customtkinter

def createWindow(width, height):
    app = customtkinter.CTk()
    app.geometry(f"{width}x{height}")
    return app
