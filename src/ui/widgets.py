# import customtkinter
import tkinter as tk
from tkinter import PhotoImage
import base64
from io import BytesIO


def create_button(app, text, command):
    button = tk.Button(app, text=text, command=command)
    button.pack(anchor="w", padx=10, pady=10)
    return button


def create_data_frame(app):
    frame = tk.Frame(app, bg="#262626")
    frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

    return frame


def create_label(app, text, bg="#262626"):
    label = tk.Label(app, text=text, font=("Arial", 14), bg=bg, fg="white")
    label.pack(anchor="w", padx=10, pady=5)
    return label


def create_user_post(frame, user_data):
    """Creates a user post on the GUI."""

    user_frame = tk.Frame(frame, bg="#262626", bd=2, relief=tk.RIDGE, padx=10, pady=10)
    user_frame.pack(fill="x", pady=5)

    try:
        avatar_data = base64.b64decode(user_data["avatar"])
        avatar_image = PhotoImage(data=BytesIO(avatar_data).read())
    except Exception as e:
        avatar_image = None

    if avatar_image:
        avatar_image = avatar_image.subsample(6, 6)  # Adjust size to be smaller

    avatar_label = tk.Label(user_frame, image=avatar_image, bg="#262626")
    if avatar_image:
        avatar_label.image = avatar_image
    avatar_label.pack(side="left", padx=10)

    text_frame = tk.Frame(user_frame, bg="#262626")
    text_frame.pack(side="left", fill="both", expand=True)

    name_label = tk.Label(text_frame, text=user_data["name"], bg="#262626", fg="white", font=("Arial", 14, "bold"))
    name_label.pack(anchor="w")

    quote_label = tk.Label(text_frame, text=f"{user_data['quote']}", bg="#262626", fg="white", font=("Arial", 12))
    quote_label.pack(anchor="w")

    return user_frame