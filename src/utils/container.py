import punq as punq

from src.accounts.dependencies import AccountCreateDependency
from src.transactions.dependencies import TransactionCreateDependency
from src.utils.repository import AbcRepository
from src.utils.dependencies import GetListDependency, RetrieveDependency, DeleteDependency
from src.users.dependencies import UserCreateDependency
from src.budgets.dependencies import BudgetCreateDependency
from src.categories.dependencies import CategoryCreateDependency
from src.expenses.dependencies import ExpenseCreateDependency


def get_container(repository: type[AbcRepository]) -> punq.Container:
    container = punq.Container()

    container.register(AbcRepository, repository, instance=repository())

    container.register(GetListDependency)
    container.register(RetrieveDependency)
    container.register(DeleteDependency)

    container.register(UserCreateDependency)

    container.register(AccountCreateDependency)

    container.register(TransactionCreateDependency)

    container.register(CategoryCreateDependency)

    container.register(BudgetCreateDependency)

    container.register(ExpenseCreateDependency)

    return container
