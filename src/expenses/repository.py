from sqlalchemy.orm import Session

from src.expenses import schemas
from src.models import Expense
from src.utils.repository import BaseRepository


class ExpenseRepo(BaseRepository):
    model = Expense
    session = Session
    schema = schemas.Expense
