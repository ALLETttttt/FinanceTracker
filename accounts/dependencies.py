from fastapi import Depends
from sqlalchemy.orm import Session

from accounts.schemas import CreateAccount, Account
from database import get_db
from utils.dependencies import BaseDependency


class AccountCreateDependency(BaseDependency):

    def __call__(self, body: CreateAccount, session: Session = Depends(get_db)):
        self.repo.session = session
        self.repo.model = Account
        return self.repo.create(body)
