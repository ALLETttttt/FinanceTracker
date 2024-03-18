from sqlalchemy.orm import Session

from src.accounts import schemas
from src.models import Account
from src.utils.repository import BaseRepository


class AccountRepo(BaseRepository):
    model = Account
    session = Session
    schema = schemas.Account
