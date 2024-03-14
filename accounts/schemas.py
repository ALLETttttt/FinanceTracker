
from utils.config_schema import ConfigSchema


class BaseAccount(ConfigSchema):
    account_name: str


class Account(BaseAccount):
    pass


class CreateAccount(BaseAccount):
    pass
