# import customtkinter
import tkinter as tk
from tkinter import PhotoImage
import base64
from io import BytesIO


class Colors:
    """Color constants for the GUI."""

    BACKGROUND = "#262626"
    WINDOW = "#25282c"
    TEXT = "white"


def create_button(app, text, command):
    button = tk.Button(app, text=text, command=command)
    button.configure(bg=Colors.BACKGROUND, fg=Colors.TEXT)
    button.pack(anchor="w", padx=10, pady=10)
    return button


def create_data_frame(app):
    frame = tk.Frame(app, bg=Colors.BACKGROUND)
    frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

    return frame

def create_frame(app):
    frame = tk.Frame(app, bg=Colors.BACKGROUND)
    frame.pack(pady=10)
    return frame


def create_label(app, text, bg=Colors.BACKGROUND):
    label = tk.Label(app, text=text, font=("Arial", 14), bg=bg, fg=Colors.TEXT)
    label.pack(anchor="w", padx=10, pady=5)
    return label


def create_window(width, height):
    window = tk.Tk()

    screen_width = window.winfo_screenwidth()

    x_position = (screen_width - width) // 2
    y_position = 100
    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

    window.configure(bg="#25282c")
    return window


def crete_entry(app, default):
    entry = tk.Entry(app)
    if default:
        entry.insert(0, default)

    entry.configure(bg=Colors.BACKGROUND, fg=Colors.TEXT)
    entry.configure(font=("Arial", 14))

    entry.pack()
    return entry


def create_user_post(frame, user_data):
    user_frame = tk.Frame(
        frame, bg=Colors.BACKGROUND, bd=2, relief=tk.RIDGE, padx=10, pady=10
    )
    user_frame.pack(fill="x", pady=5)

    try:
        avatar_data = base64.b64decode(user_data["avatar"])
        avatar_image = PhotoImage(data=BytesIO(avatar_data).read())
    except Exception as e:
        avatar_image = None

    if avatar_image:
        avatar_image = avatar_image.subsample(6, 6)

    avatar_label = tk.Label(user_frame, image=avatar_image, bg=Colors.BACKGROUND)
    if avatar_image:
        avatar_label.image = avatar_image
    avatar_label.pack(side="left", padx=10)

    text_frame = tk.Frame(user_frame, bg=Colors.BACKGROUND)
    text_frame.pack(side="left", fill="both", expand=True)

    name_label = tk.Label(
        text_frame,
        text=user_data["name"],
        bg=Colors.BACKGROUND,
        fg=Colors.TEXT,
        font=("Arial", 14, "bold"),
    )
    name_label.pack(anchor="w")

    quote_label = tk.Label(
        text_frame,
        text=f"{user_data['quote']}",
        bg=Colors.BACKGROUND,
        fg=Colors.TEXT,
        font=("Arial", 12),
    )
    quote_label.pack(anchor="w")

    source_label = tk.Label(
        text_frame,
        text=f"Source: {user_data['source']}",
        bg=Colors.BACKGROUND,
        fg=Colors.TEXT,
        font=("Arial", 10),
    )

    source_label.pack(anchor="w")

    return user_frame
