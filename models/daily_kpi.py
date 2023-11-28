""""""

from models.base_model import OrmBase, BaseModel
from models.goal import Goal
from models.sub_goal import SubGoal
from sqlalchemy import Integer, String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship


class DailyKPI(OrmBase, BaseModel):
    """Represents the daily goals that will be mapped to the DailyKPI table"""

    __tablename__ = 'daily-kpi'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    goal_id = Column(Integer, ForeignKey('goals.id'), nullable=False)
    sub_goal_id = Column(Integer, ForeignKey('sub_goals.id'), nullable=False)

    def __init__(self, ) -> None:
        """Initialising a daily kpi."""