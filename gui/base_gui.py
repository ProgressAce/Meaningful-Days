"""Defines a class for creating the gui."""

import customtkinter as ctk


class BaseGUI(ctk.CTkFrame):
    """Represents the gui of the application."""

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    def __init__(self, root):
        """Initialising the gui."""

        self.colour1 = "#222448"
        self.colour2 = "#54527E"
        self.colour3 = "WHITE"

        super().__init__(root, bg_color=self.colour1)

        self.root_frame = self
        self.root_frame.pack(fill=ctk.BOTH, expand=True)
        self.root_frame.columnconfigure(0, weight=1)
        self.root_frame.rowconfigure(0, weight=1)

        self.load_welcome_screen()

    def load_welcome_screen(self):
        """Create and load the welcome screen."""
        self.welcome_frame = ctk.CTkFrame(self.root_frame)
        self.current_frame = self.welcome_frame

        self.welcome_frame.columnconfigure(0, weight=1)
        self.welcome_frame.rowconfigure(0, weight=1)
        self.welcome_frame.rowconfigure(1, weight=1)
        self.welcome_frame.rowconfigure(2, weight=2)
        self.welcome_frame.grid(column=0, row=0, sticky="nsew")  # place welcome frame

        self.heading_label = ctk.CTkLabel(
            self.welcome_frame,
            text="Structuring Life",
            font=("Freestyle Script", 70),  # Gabriola or Forte
        )
        self.heading_label.grid(column=0, row=0, pady=2, sticky="nsew")  # place on grid

        self.slogan_label = ctk.CTkLabel(
            self.welcome_frame,
            text="~ Taking control of your life & the simple things",
            font=("Gabriola", 26),
        )
        self.slogan_label.grid(column=0, row=1, sticky="n")  # place on grid

        self.start_button = ctk.CTkButton(
            self.welcome_frame,
            text="Let's get to work!",  # add puffed out super man chest pose emoticon
            font=("Gabriola", 35),
            height=250,
            width=300,
        )
        self.start_button.grid(column=0, row=2, pady=5, sticky="n")  # place on grid

    def remove_frame(self, frame):
        """Removes a frame and all the widgets it contains."""

        for child in frame.winfo_children():
            child.destroy()


if __name__ == "__main__":
    ui = ctk.CTk()
    ui.geometry("700x500")
    ui.resizable(width=None, height=None)
    gui_obj = BaseGUI(ui)
    ui.mainloop()
