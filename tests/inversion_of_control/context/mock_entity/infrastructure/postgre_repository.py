from summer.inversion_of_control.dependencies import service
from tests.inversion_of_control.context.mock_entity.core.i_repository import IRepository


@service()
class PostgreRepository(IRepository):
    def custom_method(self):
        return "Postgre respoistory"
