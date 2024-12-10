import customtkinter


def create_button(app, text, command):
    button = customtkinter.CTkButton(app, text=text, command=command)
    button.pack(padx=20, pady=20)
    return button


def create_data_frame(app, target, row, col, colspan=1):
    frame = customtkinter.CTkFrame(app, corner_radius=10)

    frame.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10, sticky="nsew")

    title_label = customtkinter.CTkLabel(frame, text=target, font=("Arial", 16, "bold"))

    title_label.pack(anchor="w", padx=10, pady=(5, 0))

    return frame


def create_label(app, text):
    label = customtkinter.CTkLabel(app, text=text, font=("Arial", 14))
    label.pack(anchor="w", padx=10, pady=5)
    return label
