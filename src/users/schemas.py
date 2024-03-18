from src.accounts.schemas import AccountResponse
from src.budgets.schemas import BudgetResponse
from src.expenses.schemas import ExpenseResponse
from src.utils.config_schema import ConfigSchema


class BaseUser(ConfigSchema):
    username: str
    email: str
    password: str


class CreateUser(BaseUser):
    pass


class User(BaseUser):
    id: int
    accounts: list[AccountResponse]
    budgets: list[BudgetResponse]
    expenses: list[ExpenseResponse]


