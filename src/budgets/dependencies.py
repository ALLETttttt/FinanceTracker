from fastapi import Depends
from sqlalchemy.orm import Session

from src.budgets.schemas import CreateBudget
from src.database import get_db
from src.utils.dependencies import BaseDependency


class BudgetCreateDependency(BaseDependency):

    def __call__(self, body: CreateBudget, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.create(body)