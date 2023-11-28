"""Defines a class for handling database storage."""

from models.base_model import BaseModel, OrmBase
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker,  scoped_session

class DBStorage:
    """Connects to MySQL database and handles operations using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self) -> None:
        """Instantiate DBStorage object and establish a database connection"""
        self.__engine = create_engine('sqlite:///sqlite_database.db')

    def reload(self):
        """Uploads table data to the database and prepares session object."""
        OrmBase.metadata.create_all()
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def new(self, obj):
        """Adds a new object/record to the table."""
        self.__session.add(obj)

    def save(self):
        """Commits changes or objects to the session object."""
        self.__session.commit()