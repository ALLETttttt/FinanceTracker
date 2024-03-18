from sqlalchemy.orm import Session

from src.categories import schemas
from src.models import Category
from src.utils.repository import BaseRepository


class CategoryRepo(BaseRepository):
    model = Category
    session = Session
    schema = schemas.Category
