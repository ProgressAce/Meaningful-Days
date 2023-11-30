"""Defines a class to serve as a base class for SQLAlchemy ORM mapping."""

from datetime import date
from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base
import models

OrmBase = declarative_base()


class BaseModel:
    """Serves as the base class for classes undergoing ORM mapping"""

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    created_date = Column(DateTime, default=date.today())
    target_date = Column(DateTime, nullable=False)
    completed_date = Column(DateTime, default=None, nullable=True)
    status = Column(String(10), default="active")

    def __init__(self, title, target_date):
        """Initialising an object."""
        # validate arguments elsewhere
        self.title = title
        self.target_date = target_date

    def __str__(self):
        """Informal string representation for daily_kpi object"""
        return self.__class__.__name__

    def save(self):
        """Adds and commits the current object to the database."""
        models.db.new(self)
        models.db.save()

    def delete(self):
        """Deletes the current object from the database."""

    def mark_complete(self, completed_date):
        """Checks an object as complete."""
        # validate argument
        #
        self.completed_date = completed_date
        self.status = "inactive"


if __name__ == "__main__":
    print(
        "Let's get this started and sonn ready for testing, deployment and production"
    )
