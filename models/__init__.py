"""Prepares SQLite database storage engine for the project."""

from models.storage.db import DBStorage

db = DBStorage()
db.reload()
