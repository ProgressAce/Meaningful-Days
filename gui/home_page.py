"""Defines the gui page that will act as the base for other pages."""

from functools import partial
import customtkinter as ctk
from gui.goal_frame import GoalFrame
from gui.kpi_frame import KPIFrame


class HomeGUI:
    """Reperesents the home page of the Graphical User Interface."""

    def __init__(self, ctk_root_frame):
        """Initialises the home screen gui."""
        self.root_frame = ctk_root_frame
        self.home_frame = ctk.CTkFrame(ctk_root_frame, fg_color="#fceab8")
        self.home_frame.rowconfigure(0, weight=0)
        self.home_frame.rowconfigure(1, weight=0)
        self.home_frame.rowconfigure(2, weight=4)
        self.home_frame.grid(column=0, row=0, sticky="nsew")
        self.column_num = 0
        self.current_info_frame = None

    def remove_frame(self, frame):
        """Removes a frame and all the widgets it contains."""

        if frame:
            for child in frame.winfo_children():
                child.destroy()
            frame.destroy()

    def load_home_screen(self):
        """Create and load the home screen."""

        self.load_home_buttons()

        home_lbl = ctk.CTkLabel(
            self.home_frame,
            text="Structured Living",
            font=("Freestyle Script", 40),
            text_color="orange",
            fg_color="black",
        )
        home_lbl.grid(
            column=round(self.column_num / 2) - 1, row=0, columnspan=2, pady=10
        )

    def load_home_buttons(self):
        """Create and load the buttons for the home screen."""
        buttons = {"Goals": GoalFrame, "KPI": KPIFrame}
        button_num = len(buttons)

        # there should be two added columns for number of buttons
        # for better centering
        self.column_num = button_num + 2
        for i in range(self.column_num):
            self.home_frame.columnconfigure(i, weight=1)

        index = 1
        for btn_name, clss in buttons.items():
            cls_with_args = partial(
                clss, self.home_frame, self.current_info_frame, self.column_num
            )
            button = ctk.CTkButton(
                self.home_frame,
                height=38,
                text=btn_name,
                font=("Arial", 27),
                corner_radius=50,
                command=cls_with_args,
                fg_color="grey",
            )
            button.grid(column=index, row=1, pady=14, sticky="n")
            index += 1
