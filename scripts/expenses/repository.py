from sqlalchemy.orm import Session

from scripts.expenses import schemas
from models import Expense
from utils import BaseRepository


class ExpenseRepo(BaseRepository):
    model = Expense
    session = Session
    schema = schemas.Expense
