import threading
import customtkinter

def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("800x800")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

def run():
    app.mainloop()


if __name__ == "__main__":
    run()
