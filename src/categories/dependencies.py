from fastapi import Depends
from sqlalchemy.orm import Session

from src.categories.schemas import CreateCategory
from src.database import get_db
from src.utils.dependencies import BaseDependency


class CategoryCreateDependency(BaseDependency):

    def __call__(self, body: CreateCategory, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.create(body)
