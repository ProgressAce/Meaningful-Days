"""Testing for the BaseModel class."""

import sys
import unittest
from datetime import date
from models import base_model
import models

BaseModel = base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Unit tests to ensure documentation and style for base_model module."""

    def test_module_doc(self):
        """Test that module docstring is present."""

        self.assertIsNot(base_model.__doc__, None, "base_model.py needs a docstring")
        self.assertTrue(len(base_model.__doc__) > 5, "base_model.py needs a docstring")

    def test_class_doc(self):
        """Test that a BaseModel class docstring is present."""

        class_doc = BaseModel.__doc__
        self.assertIsNot(class_doc, None, "BaseModel needs a docstring")
        self.assertTrue(len(class_doc) > 5, "BaseModel needs a docstring")

    def test_this_module_doc(self):
        """Test that this module's docstring is present."""

        mod_docs = sys.modules[__name__].__doc__
        self.assertIsNot(mod_docs, None, "Test module needs a docstring")
        self.assertTrue(len(mod_docs) > 5, "Test module needs a docstring")


class TestBaseModel(unittest.TestCase):
    """Tests to ensure BaseModel class works and acts as it should."""

    def setUp(self):
        """Test setup for the BaseModel class."""
        self.bm = BaseModel("goal1", date(2023, 12, 31))
        self.bm2 = BaseModel("goal2", date(2023, 12, 15))

    def test_instantiation(self):
        """Test that a BaseModel objects is created correctly."""

        self.assertIsInstance(
            self.bm, BaseModel, "The object should be a BaseModel one."
        )
        self.assertIsInstance(
            self.bm2, BaseModel, "The object should be a BaseModel one."
        )


# session objects don't seem to be tested correctly by unittests
# def test_save(self):
#     """Test ensuring the correct working of the save method."""

#     old_total = len(models.db.all(base_model.BaseModel))
#     self.bm.save()
#     new_total = len(models.db.all(base_model.BaseModel))
#     self.assertGreater(new_total, old_total)
