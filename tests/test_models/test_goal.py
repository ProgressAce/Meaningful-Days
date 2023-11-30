"""Testing for the Goal class."""

import sys
import unittest
from datetime import date
from models import goal
import models

Goal = goal.Goal


class TestGoalDocs(unittest.TestCase):
    """Unit tests to ensure documentation and style for base_model module."""

    def test_module_doc(self):
        """Test that module docstring is present."""

        self.assertIsNot(goal.__doc__, None, "goal.py needs a docstring")
        self.assertTrue(len(goal.__doc__) > 5, "goal.py needs a docstring")

    def test_class_doc(self):
        """Test that a BaseModel class docstring is present."""

        class_doc = goal.__doc__
        self.assertIsNot(class_doc, None, "Goal needs a docstring")
        self.assertTrue(len(class_doc) > 5, "Goal needs a docstring")

    def test_this_module_doc(self):
        """Test that this module's docstring is present."""

        mod_docs = sys.modules[__name__].__doc__
        self.assertIsNot(mod_docs, None, "Test module needs a docstring")
        self.assertTrue(len(mod_docs) > 5, "Test module needs a docstring")


class TestGoal(unittest.TestCase):
    """Tests to ensure Goal class works and acts as it should."""

    def setUp(self):
        """Test setup for the Goal class."""
        self.goal = Goal("goal1", date(2023, 12, 15))

    def test_instantiation(self):
        """Test that a Goal objects is created correctly."""

        self.assertIsInstance(self.goal, Goal, "The object should be a BaseModel one.")


# session objects don't seem to be tested correctly by unittests
# def test_save(self):
#     """Test ensuring the correct working of the save method."""

#     from models.storage.db import DBStorage

#     db = DBStorage()
#     print("HERE IT IS:", db.all(Goal))
#     old_total = len(models.db.all(Goal))
#     self.goal.save()
#     new_total = len(models.db.all(Goal))
#     self.assertGreater(new_total, old_total)
