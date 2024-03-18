from src.budgets.schemas import BudgetResponse
from src.transactions.schemas import TransactionResponse
from src.utils.config_schema import ConfigSchema


class BaseCategory(ConfigSchema):
    category_name: str


class Category(BaseCategory):
    id: int
    transactions: list[TransactionResponse]
    budgets: list[BudgetResponse]


class CreateCategory(BaseCategory):
    pass

