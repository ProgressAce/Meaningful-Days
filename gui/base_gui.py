"""Defines a class for creating the gui."""

import customtkinter as ctk
from gui.home_page import HomeGUI


class BaseGUI(ctk.CTk):
    """Represents the gui of the application."""

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    def __init__(self):
        """Initialises the base gui."""
        super().__init__()

        # BaseGUI.root_frame will serve as the base for all frames to rest upon
        self.root_frame = ctk.CTkFrame(self)
        self.root_frame.pack(fill=ctk.BOTH, expand=True)
        self.root_frame.columnconfigure(0, weight=1)
        self.root_frame.rowconfigure(0, weight=1)

        self.load_welcome_screen()

    def load_welcome_screen(self):
        """Create and load the welcome screen."""
        self.welcome_frame = ctk.CTkFrame(self.root_frame, fg_color="#fceab8")

        self.welcome_frame.columnconfigure(0, weight=1)
        self.welcome_frame.rowconfigure(0, weight=1)
        self.welcome_frame.rowconfigure(1, weight=1)
        self.welcome_frame.rowconfigure(2, weight=2)
        self.welcome_frame.grid(column=0, row=0, sticky="nsew")  # place welcome frame

        heading_label = ctk.CTkLabel(
            self.welcome_frame,
            text="Structuring Life",
            font=("Freestyle Script", 70),  # Gabriola or Forte
            text_color="orange",
        )
        heading_label.grid(column=0, row=0, pady=2, sticky="nsew")  # place on grid

        slogan_label = ctk.CTkLabel(
            self.welcome_frame,
            text="~ Taking control of your life & the simple things",
            font=("Gabriola", 26),
        )
        slogan_label.grid(column=0, row=1, sticky="n")  # place on grid

        start_button = ctk.CTkButton(
            self.welcome_frame,
            text="Let's get to work!",  # add puffed out super man chest pose emoticon
            font=("Gabriola", 35),
            height=250,
            width=300,
            command=self.load_home_screen,
        )
        start_button.grid(column=0, row=2, pady=5, sticky="n")  # place on grid

    def load_home_screen(self):
        """Enters the GUI Home Screen class."""
        home_page = HomeGUI(ctk_root_frame=self.root_frame)

        self.remove_frame(self.welcome_frame)
        home_page.load_home_screen()

    def remove_frame(self, frame):
        """Removes a frame and all the widgets it contains."""

        for child in frame.winfo_children():
            child.destroy()
        frame.destroy()


# if __name__ == "__main__":
#     import customtkinter as ctk
#     from home_page import HomeGUI

#     ui = BaseGUI()
#     ui.title("Structured Living")
#     ui.geometry("700x500")
#     ui.resizable(width=None, height=None)
#     ui.mainloop()
