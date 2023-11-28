"""Defines a class to serve as a base class SQLAlchemy ORM mapping."""

from datetime import datetime
from models import db
from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.ext.declarative import declaritive_base

OrmBase = declaritive_base()

class BaseModel():
    """Serves as the base class for classes undergoing ORM mapping"""

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    created_date = Column(DateTime, default=datetime.now())
    target_date = Column(DateTime, nullable=False)
    completed_date = Column(DateTime, default=None, nullable=True)
    status = Column(String(10), default='active')

    def __init__(self, title, target_date) -> None:
        """Initialising an object."""
        # validate arguments
        try:
            if not isinstance(title, str):
                raise TypeError('Your title should be completed.')
            if len(title) < 1:
                raise ValueError
            
            if not isinstance(target_date, datetime):
                raise TypeError('Your target date should be set.')
            if target_date < self.created_date:
                raise ValueError('')
        except (TypeError, ValueError):
            pass
        else:
            self.title = title
            self.target_date = target_date

    def save(self):
        """Adds and commits the current object to the database."""
        db.new(self)
        db.save()

    def delete(self):
        """Deletes the current object from the database."""

    def mark_complete(self, completed_date):
        """Checks an object as complete."""
        # validate argument
        #
        self.completed_date = completed_date
        self.status = 'inactive'

if __name__ == '__main__':
    print("Let's get this started and sonn ready for testing, deployment and production")