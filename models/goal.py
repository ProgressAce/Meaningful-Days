"""Defines the Goal class for SQLAlchemy ORM mapping."""

from sqlalchemy.orm import relationship
from models.base_model import OrmBase, BaseModel


class Goal(OrmBase, BaseModel):
    """Goal representation to be mapped to a database table."""

    __tablename__ = 'goals'
    sub_goals = relationship('SubGoal', backref='goal')
    daily_kpis = relationship('DailyKPI', backref='goal')

    def __init__(self, title, target_date):
        """Initialising a goal."""
        super().__init__(title=title, target_date=target_date)
