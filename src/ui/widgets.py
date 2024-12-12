# import customtkinter
import tkinter as tk


def create_button(app, text, command):
    button = tk.Button(app, text=text, command=command)
    button.pack(anchor="w", padx=10, pady=10)
    return button


def create_data_frame(app):
    frame = tk.Frame(app,  bg="#262626")

    frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

    return frame


def create_label(app, text, bg="#262626"):
    label = tk.Label(app, text=text, font=("Arial", 14), bg=bg, fg="white")
    label.pack(anchor="w", padx=10, pady=5)
    return label
