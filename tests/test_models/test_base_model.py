"""Testing for the BaseModel class."""

from datetime import datetime
from models import base_model
import pep8
import sys
import unittest
BaseModel = base_model.BaseModel
module_doc = base_model.__docs__


class TestBaseModelDocs(unittest.TestCase):
    """Unit tests to ensure documentation and style for base_model module."""

    # def test_pep8_compliance(self):
    #     """Test that the base_model.py module follows pep8 standards."""

    #     paths = ('models/base_model.py', 'tests/test_models/test_base_model.py')
    #     for path in paths:
    #         with self.subTest(path):
    #             num_errors = pep8.Checker(path).check_all()
    #             self.assertEqual(num_errors, 0)

    def test_module_doc(self):
        """Test that module docstring is present."""

        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 5,
                        "base_model.py needs a docstring")

    def test_class_doc(self):
        """Test that a BaseModel class docstring is present."""

        class_doc = BaseModel.__doc__
        self.assertIsNot(class_doc, None,
                         "BaseModel needs a docstring")
        self.assertTrue(len(class_doc) > 5,
                        "BaseModel needs a docstring")

    def test_this_module_doc(self):
        """Test that this module's docstring is present."""

        mod_docs = sys.modules[__name__].__doc__
        self.assertIsNot(mod_docs, None,
                         "Test module needs a docstring")
        self.assertTrue(len(mod_docs) > 5,
                        "Test module needs a docstring")
        

class TestBaseModel(unittest.TestCase):
    """Tests to ensure BaseModel class works and acts as it should."""

    def setUp(self):
        """Test setup for the BaseModel class."""
        self.bm = BaseModel()
        self.bm2 = BaseModel()

    def test_instantiation(self):
        """Test that a BaseModel objects is created correctly."""

        self.assertIsInstance(self.bm, BaseModel,
                              "The object should be a BaseModel one.")
        self.assertIsInstance(self.bm2, BaseModel,
                              "The object should be a BaseModel one.")
        
    def test_save(self):
        """Test ensuring the correct working of the save method."""

        total_goals = self.storage._DBStorage__session.query(Goal).count()
        self.storage.save()
        new_total = self.storage._DBStorage__session.query(Goal).count()
        self.assertGreater(new_total, total_goals)