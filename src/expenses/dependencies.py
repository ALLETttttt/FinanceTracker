from fastapi import Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.expenses.schemas import CreateExpense
from src.utils.dependencies import BaseDependency


class ExpenseCreateDependency(BaseDependency):

    def __call__(self, body: CreateExpense, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.create(body)
