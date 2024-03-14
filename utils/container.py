import punq as punq

from utils.repository import AbcRepository
from utils.dependencies import GetListDependency, RetrieveDependency, DeleteDependency


def get_container(repository: type[AbcRepository]) -> punq.Container:
    container = punq.Container()

    container.register(AbcRepository, repository, instance=repository())

    container.register(GetListDependency)
    container.register(RetrieveDependency)
    container.register(DeleteDependency)

    return container
