"""Creates the goal frame interface."""

from datetime import date
from functools import partial
from tkinter import messagebox
import customtkinter as ctk
import tkcalendar as tkcal
from models.goal import Goal
from models.sub_goal import SubGoal
import models
import re


class GoalFrame:
    """Represents the goal frame interface of the home page."""

    def __init__(self, home_frame, current_frame, column_num):
        """Initialisation of goalframe object.

        Args:
            home_frame(ctk.Frame): the home_page frame that will serve
                    as the root frame.
            current_frame(ctk.Frame): the frame currently in use on
                    the home_frame.
            column_num(int): the total column number of home_frame"""

        # for goal_frame
        self.home_frame = home_frame
        self.current_frame = current_frame
        self.column_num = column_num

        # for goal_frame's add_frame
        self.current_add_frame = None

        # for checking if information is being added
        self.info_status = "success"

        self.load_goal_frame()

    def remove_frame(self, frame):
        """Removes a frame and all the widgets it contains."""

        if frame:
            for child in frame.winfo_children():
                child.destroy()
            frame.destroy()

    def on_close(self, window, info_status):
        """Handles event when window is exited.

        The current_add_frame is set to None so that when the add_window is closed
        and reopened, the current_add_frame won't hold onto parent window
        which was destroyed on exit.
        """

        if info_status == "pending":
            if messagebox.askokcancel(
                "Closing the current window",
                "Are you certain you want to close it? Unsaved information will be lost.",
            ):
                self.current_add_frame = None
                window.destroy()

    def center(self, top_window):
        """Finds the center of the screen and centers the toplevel window."""
        pass

    def load_goal_frame(self):
        """Create and load the goal frame."""

        self.remove_frame(self.current_frame)

        goal_frame = ctk.CTkFrame(
            self.home_frame,
            fg_color="#fceab8",
            border_width=2,
            border_color="grey",
        )
        # columnconfig
        goal_frame.columnconfigure(0, weight=1)
        goal_frame.columnconfigure(1, weight=1)
        goal_frame.columnconfigure(2, weight=1)
        goal_frame.columnconfigure(3, weight=1)
        goal_frame.rowconfigure(0, weight=0)
        goal_frame.rowconfigure(1, weight=0)
        goal_frame.grid(
            column=0, row=2, columnspan=self.column_num, padx=10, pady=10, sticky="nsew"
        )

        self.current_frame = goal_frame

        self.display_goals_subgoals(goal_frame)

        goal_adding_method = partial(self.goal_adding_layout, goal_frame)

        # frame for holding all the buttons
        # button_frame = ctk.CTkFrame(
        #     goal_frame,
        #     fg_color="#fceab8",
        #     border_width=2,
        #     border_color="grey",
        # )
        # button_frame.columnconfigure(0, weight=1)
        # button_frame.columnconfigure(1, weight=1)
        # button_frame.columnconfigure(2, weight=1)
        # button_frame.columnconfigure(3, weight=1)
        # button_frame.grid(column=0, row=0, columnspan=2, sticky='nsew')

        # button for adding a new goal
        add_btn = ctk.CTkButton(
            goal_frame,
            width=200,
            height=30,
            border_width=2,
            text="Add goal/subgoal",
            font=("Arial", 16),
            command=goal_adding_method,
        )
        add_btn.grid(column=4, row=0, padx=5, pady=5)

    def get_active_goals_subgoals(self, clss):
        """Returns a list of all the active goals/subgoals from the database."""

        objectives = models.db.all(clss)
        active_objectives = []
        for obj in objectives:
            if obj.status == "active":
                active_objectives.append(obj)

        return active_objectives

    def display_goals_subgoals(self, goal_frame):
        """Creates the widgets for displaying a list of all the active goals.
        All the goals are taken from the storage system."""

        text_display = ctk.CTkTextbox(
            goal_frame, fg_color="#fceab8", font=("Cambria", 20)
        )
        text_display.grid(
            column=0, row=2, columnspan=6, sticky="nsew", padx=15, pady=15
        )
        goal_frame.rowconfigure(2, weight=4)

        # additional text insertion styles
        # creating placeholders for text to have certain styles
        # text_display.tag_add("heading", ctk.END)
        # text_display.tag_config("heading", font=("Times New Roman", 35, "bold"))
        # text_display.tag_config("goals", font=("Cambria", 28))
        # text_display.tag_config("subgoals", font=("Cambria", 24))
        # text_display.tag_config("time-left", font=("Cambria", 26, "italic"))

        # tab works as intended - text_display.insert("0.0", "Active Goals & Subgoals\n\n\tmr.Tab\n")
        text_display.insert("0.0", "Active Goals & Subgoals\n\n")

        goals = self.get_active_goals_subgoals(Goal)
        for i, goal in enumerate(goals):
            text_display.insert(ctk.END, f"({i + 1}). {goal.title}")
            text_display.insert(ctk.END, f"    Target date: {goal.get_target_date()}\n")

            for subgoal in goal.sub_goals:
                text_display.insert(ctk.END, f"~~ {subgoal.title}")
                text_display.insert(
                    ctk.END, f"    Target date: {subgoal.get_target_date()}\n"
                )

            text_display.insert(ctk.END, "\n")

        text_display.configure(state="disabled")

    def goal_adding_layout(self, goal_frame):
        """Creates the widgets for adding goals and subgoals"""

        add_window = ctk.CTkToplevel(goal_frame, fg_color="#fceab8", takefocus=True)
        add_window.title("Add new goal or subgoal")
        add_window.geometry("950x650")
        add_window.columnconfigure(0, weight=1)
        add_window.columnconfigure(1, weight=1)
        add_window.rowconfigure(0, weight=0)
        add_window.rowconfigure(1, weight=0)
        add_window.rowconfigure(2, weight=2)
        # self.center(add_window)

        selection_lbl = ctk.CTkLabel(
            add_window,
            text="Select whether to add a new 'Goal' or a 'Subgoal'",
            font=("Arial", 16),
        )
        selection_lbl.grid(column=0, row=0, columnspan=2, pady=18)

        radio_var = ctk.StringVar(add_window, value="none")
        add_form_method = partial(self.add_form, add_window, radio_var)

        # Radio buttons for picking between goal and subgoal
        goal_rad = ctk.CTkRadioButton(
            add_window,
            text="New Goal",
            value="goal",
            variable=radio_var,
            command=add_form_method,
        )
        goal_rad.grid(column=0, row=1, pady=5, padx=6)

        subgoal_rad = ctk.CTkRadioButton(
            add_window,
            text="New Subgoal",
            value="subgoal",
            variable=radio_var,
            command=add_form_method,
        )
        subgoal_rad.grid(column=1, row=1, pady=5, padx=6)

    def add_form(self, add_window, radio_var):
        """Create the widgets for entering information for a new goal."""

        self.info_status = "pending"
        # handles the event of the add window closing
        on_close_method = partial(self.on_close, add_window, self.info_status)
        add_window.protocol("WM_DELETE_WINDOW", on_close_method)

        self.remove_frame(self.current_add_frame)

        add_frame = ctk.CTkFrame(
            add_window,
            fg_color="#fceab8",
            border_width=1,
            border_color="black",
        )
        add_frame.columnconfigure(0, weight=1)
        add_frame.columnconfigure(1, weight=1)
        add_frame.grid(column=0, row=2, columnspan=2, sticky="nsew", pady=14, padx=12)

        self.current_add_frame = add_frame

        # the widgets for entering the information of a new goal/subgoal
        title_entry = ctk.CTkEntry(
            add_frame,
            height=42,
            width=300,
            placeholder_text="...that you have decided to dedicate yourself to",
        )
        title_entry.grid(column=0, row=1, pady=2, padx=12)

        target_calendar = tkcal.Calendar(
            add_frame, selectmode="day", date_pattern="y-mm-dd"
        )
        target_calendar.grid(column=0, row=3, pady=12, padx=12, rowspan=3)

        # defining variables and widgets based on radio button selection
        if radio_var.get() == "goal":
            goal_text = "Enter the new goal:"
            submit_btn_text = "Submit new goal '~'"
            submit_command = partial(
                self.create_new_goal, title_entry, target_calendar, add_window
            )

        elif radio_var.get() == "subgoal":
            goal_text = "Enter the new subgoal:"

            goal_selection_lbl = ctk.CTkLabel(
                add_frame,
                text="Select the main end goal for your new subgoal:",
                font=("Arial", 16),
                justify=ctk.CENTER,
            )
            goal_selection_lbl.grid(column=1, row=0, pady=12, padx=12)

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

            submit_btn_text = "Submit new subgoal '~'"
            submit_command = partial(
                self.create_new_subgoal,
                title_entry,
                target_calendar,
                goal_cmbox,
                add_window,
            )

        title_lbl = ctk.CTkLabel(
            add_frame,
            text=goal_text,
            font=("Arial", 16),
            justify=ctk.CENTER,
        )
        title_lbl.grid(column=0, row=0, pady=12, padx=12)

        target_date_lbl = ctk.CTkLabel(
            add_frame, text="Target Date for completion:", font=("Arial", 24)
        )
        target_date_lbl.grid(column=0, row=2, pady=20, padx=12)

        submit_btn = ctk.CTkButton(
            add_frame,
            width=200,
            height=38,
            text=submit_btn_text,
            command=submit_command,
        )
        submit_btn.grid(column=0, row=7, pady=10, padx=10, columnspan=2, rowspan=2)

    def create_new_goal(self, title_entry, target_calendar, add_window):
        """Inserts a new goal into the goal database table."""

        title = title_entry.get()
        target_date = target_calendar.parse_date(target_calendar.get_date())
        today = date.today()

        # validate args
        if not isinstance(title, str):
            messagebox.showerror(
                "Error",
                "The title should contain atleast some letters. We only speak ascii :(",
            )
            raise TypeError(
                "The title should contain atleast some letters. We only speak ascii :("
            )

        if len(title) < 1 or len(title) > 50:
            messagebox.showerror(
                "Error",
                "The title should be between 1 and 50 characters long.",
            )
            raise ValueError("The title should be between 1 and 50 characters long.")

        if target_date <= today:
            messagebox.showerror(
                "Error",
                "The selected target date should be a future day that has not yet come",
            )
            raise ValueError(
                "The selected target date should be a future day that has not yet come"
            )

        # ensure that there is no existing goal with the same title
        existing_goal = models.db.get_active_title(Goal, title)
        if existing_goal is not None:
            messagebox.showerror(
                "Issue creating goal.",
                "The goal you created is active and already exists. Your title name is a duplicate.",
            )
            return None

        # new goal creation and insertion into the database
        new_goal = Goal(title, target_date)
        new_goal.save()
        messagebox.showinfo(
            "Success",
            "Your new goal was created successfully. All the best in rising up to fulfill it '~'",
        )
        self.info_status = "success"
        self.remove_frame(add_window)
        self.current_add_frame = None

    def create_new_subgoal(self, title_entry, target_calendar, goal_cmbox, add_window):
        """Inserts a new subgoal into the subgoal database table."""

        title = title_entry.get()
        target_date = target_calendar.parse_date(target_calendar.get_date())
        goal_title = re.split(r"^\([0-9]+\)\. ", goal_cmbox.get(), maxsplit=1)[1]
        today = date.today()

        # validate args
        if not isinstance(title, str):
            messagebox.showerror(
                "Error",
                "The title should contain atleast some letters. We only speak ascii :(",
            )
            raise TypeError(
                "The title should contain atleast some letters. We only speak ascii :("
            )

        if len(title) < 1 or len(title) > 50:
            messagebox.showerror(
                "Error",
                "The title should be between 1 and 50 characters long.",
            )
            raise ValueError("The title should be between 1 and 50 characters long.")

        if target_date <= today:
            messagebox.showerror(
                "Error",
                "The selected target date should be a future day that has not yet come",
            )
            raise ValueError(
                "The selected target date should be a future day that has not yet come"
            )

        if goal_title is None:
            messagebox.showerror(
                "Error",
                "Please select a main goal that your new subgoal is for.",
            )
            raise ValueError("Please select a main goal that your new subgoal is for.")

        # double surity that the selected goal exists and obtaining its id
        existing_goal = models.db.get_active_title(Goal, goal_title)
        if existing_goal is None:
            messagebox.showerror(
                "Issue with selected goal.",
                "The selected goal does not exist. This is most likely due to an"
                + "error on our end and we apologise for the inconvenience.",
            )
            return None
        goal_id = existing_goal.id

        # ensure that there is no existing subgoal with the same title
        existing_subgoal = models.db.get_active_title(SubGoal, title)
        if existing_subgoal is not None:
            messagebox.showerror(
                "Issue creating subgoal.",
                "The subgoal you are trying to created is active and already exists."
                + "Change your title name so you don't create duplicate.",
            )
            return None

        # new subgoal creation and insertion into the database
        new_subgoal = SubGoal(title, target_date, goal_id)
        new_subgoal.save()
        messagebox.showinfo(
            "Success",
            "Your new goal was created successfully. All the best in rising up to fulfill it '~'",
        )
        self.info_status = "success"
        self.remove_frame(add_window)
        self.current_add_frame = None

        # list of active goals from database, dropdown menu list of
        # active subgoals belong to a specific goal
