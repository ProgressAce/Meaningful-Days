"""Testing for the DBStorage class."""

from datetime import date
from models.storage import db
from models.goal import Goal
import sys
import unittest

DBStorage = db.DBStorage
module_doc = db.__doc__


class TestDBStorageDocs(unittest.TestCase):
    """Unit tests to ensure documentation and style for db module."""

    # def test_pep8_compliance(self):
    #     """Test that the db.py module follows pep8 standards."""

    #     paths = ('models/db.py', 'tests/test_models/test_db.py')
    #     for path in paths:
    #         with self.subTest(path):
    #             num_errors = pep8.Checker(path).check_all()
    #             self.assertEqual(num_errors, 0)

    def test_module_doc(self):
        """Test that module docstring is present."""

        self.assertIsNot(module_doc, None, "db.py needs a docstring")
        self.assertTrue(len(module_doc) > 5, "db.py needs a docstring")

    def test_class_doc(self):
        """Test that a DBStorage class docstring is present."""

        class_doc = DBStorage.__doc__
        self.assertIsNot(class_doc, None, "DBStorage needs a docstring")
        self.assertTrue(len(class_doc) > 5, "DBStorage needs a docstring")

    def test_this_module_doc(self):
        """Test that this module's docstring is present."""

        mod_docs = sys.modules[__name__].__doc__
        self.assertIsNot(mod_docs, None, "Test module needs a docstring")
        self.assertTrue(len(mod_docs) > 5, "Test module needs a docstring")


class TestDBStorage(unittest.TestCase):
    """Tests to ensure DBStorage class works and acts as it should."""

    def setUp(self):
        """Test setup for the DBStorage class."""
        self.storage = DBStorage()

    def test_instantiation(self):
        """Test that a DBStorage objects is created correctly."""

        self.assertIsInstance(
            self.storage, DBStorage, "The object should be a DBStorage one."
        )

    # def test_save(self):
    #     """Test ensuring the correct working of the save method."""

    #     old_total = self.storage.all(Goal)
    #     self.storage.save()
    #     new_total = self.storage.all(Goal)
    #     self.assertGreater(new_total, old_total)


# session objects don't seem to be tested correctly by unittests
# def test_all(self):
#     """Test ensuring the correct working of the all method."""

#     records = self.storage.all(Goal)
#     self.assertIsInstance(records, list)

#     query = self.storage._DBStorage__session.query(Goal).all()
#     self.assertEqual(records, query)
