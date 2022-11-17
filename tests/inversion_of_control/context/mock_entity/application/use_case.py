from summer.inversion_of_control.dependencies import autowired
from tests.inversion_of_control.context.mock_entity.core.i_repository import IRepository


class UseCase:
    @autowired
    def __init__(self, repository: IRepository):
        self.repository = repository

    def my_use_case(self) -> str:
        return self.repository.custom_method()
