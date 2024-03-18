from sqlalchemy.orm import Session

from src.budgets import schemas
from src.models import Budget
from src.utils.repository import BaseRepository


class BudgetRepo(BaseRepository):
    model = Budget
    session = Session
    schema = schemas.Budget
