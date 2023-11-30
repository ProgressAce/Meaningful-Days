"""Defines a Sub Goal class for SQLAlchemy ORM mapping."""

from sqlalchemy import Integer, Column, ForeignKey
from models.base_model import OrmBase, BaseModel


class SubGoal(OrmBase, BaseModel):
    """Sub goal representation to be mapped to a database table."""

    __tablename__ = "sub_goals"
    goal_id = Column(Integer, ForeignKey("goals.id"), nullable=False)

    def __init__(self, title, target_date, goal_id):
        """Initialising a sub goal."""
        super().__init__(title=title, target_date=target_date)

        # validate goal_id
        if isinstance(goal_id, int) and goal_id > 0:
            self.goal_id = goal_id
        else:
            print("Goal id should be a number ")
