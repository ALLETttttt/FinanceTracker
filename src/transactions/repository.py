from sqlalchemy.orm import Session

from src.models import Transaction
from src.transactions import schemas
from src.utils.repository import BaseRepository


class TransactionRepo(BaseRepository):
    model = Transaction
    session = Session
    schema = schemas.Transaction
