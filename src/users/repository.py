from sqlalchemy.orm import Session

from src.models import User
from src.users import schemas
from src.utils.repository import BaseRepository


class UserRepo(BaseRepository):
    model = User
    session = Session
    schema = schemas.User
