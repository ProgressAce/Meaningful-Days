"""Creates the kpi frame interface."""

import customtkinter as ctk
import tkcalendar as tkcal


class KPIFrame:
    """Represents the kpi frame interface of the home page."""

    def __init__(self, home_frame, current_frame, column_num):
        """Initialisation of kpiframe object.

        Args:
            home_frame(ctk.Frame): the home_page frame that will serve
                    as the root frame.
            current_frame(ctk.Frame): the frame currently in use on
                    the home_frame.
            column_num(int): the total column number of home_frame"""

        self.home_frame = home_frame
        self.current_frame = current_frame
        self.column_num = column_num

        self.load_kpi_frame()

    def remove_frame(self, frame):
        """Removes a frame and all the widgets it contains."""

        if frame:
            for child in frame.winfo_children():
                child.destroy()
            frame.destroy()

    def get_active_goals_subgoals(self, clss):
        """Returns a list of all the active goals/subgoals from the database."""

        objectives = models.db.all(clss)
        active_objectives = []
        for obj in objectives:
            if obj.status == "active":
                active_objectives.append(obj)

        return active_objectives

    def load_kpi_frame(self):
        """Create and load the kpi frame."""

        self.remove_frame(self.current_frame)

        kpi_frame = ctk.CTkFrame(
            self.home_frame,
            fg_color="#fceab8",
            border_width=2,
            border_color="grey",
        )
        # columnconfig
        kpi_frame.columnconfigure(0, weight=1)
        kpi_frame.columnconfigure(1, weight=1)
        kpi_frame.columnconfigure(2, weight=1)
        kpi_frame.columnconfigure(3, weight=1)
        kpi_frame.grid(
            column=0, row=2, columnspan=self.column_num, padx=10, pady=10, sticky="nsew"
        )

        self.current_frame = kpi_frame

        agenda_cal = tkcal.Calendar(kpi_frame, selectmode="day", date_pattern="y-mm-dd")
        agenda_cal.grid(column=0, row=0, pady=10, padx=10, rowspan=3)

        # button for adding a new kpi
        add_btn = ctk.CTkButton(
            kpi_frame,
            width=200,
            height=30,
            border_width=2,
            text="Add day agenda",
            font=("Arial", 16),
            command=self.load_add_widgets,
        )
        add_btn.grid(column=4, row=0, padx=8, pady=8)

    def load_add_widgets(self):
        """Creates the widgets for adding a new day agenda"""

        # retrieve options for combobox
        active_goals = self.get_active_goals_subgoals(Goal)
        goal_titles = []
        for i, goal in enumerate(active_goals):
            title = f"({i + 1}). {goal.title}"
            goal_titles.append(title)

        goal_cmbox = ctk.CTkComboBox(
            add_frame, values=goal_titles, width=240, height=38
        )
        goal_cmbox.grid(column=1, row=1, pady=2, padx=12)
