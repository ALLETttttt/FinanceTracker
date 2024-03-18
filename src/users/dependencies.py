from fastapi import Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.users.schemas import CreateUser
from src.utils.dependencies import BaseDependency


class UserCreateDependency(BaseDependency):

    def __call__(self, body: CreateUser, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.create(body)
