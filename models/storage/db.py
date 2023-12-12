"""Defines a class for handling database storage."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import OrmBase
from models.goal import Goal
from models.sub_goal import SubGoal
from models.daily_kpi import DailyKPI

classes = {"Goal": Goal, "SubGoal": SubGoal, "DailyPKI": DailyKPI}


class DBStorage:
    """Connects to MySQL database and handles operations using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self) -> None:
        """Instantiate DBStorage object and establish a database connection"""
        self.__engine = create_engine("sqlite:///models/storage/sqlite.db")

    def reload(self):
        """Uploads table data to the database and prepares session object."""
        OrmBase.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        session = scoped_session(session_factory)
        self.__session = session

    def new(self, obj):
        """Adds a new object/record to the table."""
        self.__session.add(obj)

    def save(self):
        """Commits changes or objects to the session object."""
        self.__session.commit()

    def all(self, clss):
        """Queries a database session for all the rows of specified table.
        A row represents an instance, and table represents a class.

        Return:
            a list of all the rows."""

        if not isinstance(clss, str):
            if str(clss) in classes or clss in classes.values():
                q = self.__session.query(clss).all()
                return q

        return None
