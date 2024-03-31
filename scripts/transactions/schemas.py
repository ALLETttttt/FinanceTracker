from datetime import date

from utils import ConfigSchema


class BaseTransaction(ConfigSchema):
    amount: float
    description: str
    transaction_date: date


class CreateTransaction(BaseTransaction):
    account_id: int
    category_id: int


class Transaction(BaseTransaction):
    id: int


class TransactionResponse(BaseTransaction):
    id: int