"""Defines the Daily KPI class for SQLAlchemy ORM mapping."""

from sqlalchemy import Integer, String, Column, ForeignKey
from models.base_model import OrmBase, BaseModel


class DailyKPI(OrmBase, BaseModel):
    """Represents the daily goals that will be mapped to the DailyKPI table"""

    __tablename__ = 'daily_kpi'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    performance_count = Column(Integer, default=0)
    goal_id = Column(Integer, ForeignKey('goals.id'), nullable=False)
    sub_goal_id = Column(Integer, ForeignKey('sub_goals.id'), nullable=False)
    delattr(BaseModel, 'created_date')
    delattr(BaseModel, 'completed_date')
    delattr(BaseModel, 'target_date')
    delattr(BaseModel, 'status')

    def __init__(self, title, goal_id, sub_goal_id) -> None:
        """Initialising a daily kpi."""

        self.title = title
        self.goal_id = goal_id
        self.sub_goal_id = sub_goal_id

    def __str__(self):
        """Informal string representation for daily_kpi object"""
        return 'DailyKPI'
