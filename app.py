"""Defines the entry point of the application."""

from gui.base_gui import BaseGUI

# the application starts from the Graphical User Interface
ui = BaseGUI()
ui.title("Structured Living")
ui.geometry("900x650")
ui.resizable(width=False, height=False)
ui.mainloop()
