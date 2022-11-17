from tests.inversion_of_control.context.mock_entity.application.use_case import UseCase
from tests.inversion_of_control.context.setup import setup


def dependencies_test_main():
    setup()
    return UseCase().my_use_case()
