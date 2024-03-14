from models import User, Transaction
from utils.config_schema import ConfigSchema


class BaseAccount(ConfigSchema):
    account_name: str
    account_type: str


class Account(BaseAccount):
    id: int
    user_id: int
    owner: User
    transactions: list[Transaction]


class CreateAccount(BaseAccount):
    user_id: int
