""""""

from models.base_model import OrmBase, BaseModel
from models.goal import Goal
from models.sub_goal import SubGoal
from sqlalchemy import Integer, String, DateTime, Column, ForeignKey


class SubGoal(OrmBase, BaseModel):
    """Sub goal representation to be mapped to a database table."""

    __tablename__ = 'sub_goals'
    daily_performance_count = Column(Integer, default=0)
    goal_id = Column(Integer, ForeignKey('goals.id'), nullable=False)

    def __init__(self, title, target_date, goal_id):
        """Initialising a sub goal."""
        super().__init__(title, target_date)

        # validate goal_id
        if isinstance(goal_id, int) and goal_id > 0:
            self.goal_id = goal_id
        else:
            print('Goal id should be a number ')