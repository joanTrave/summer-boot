from tests.inversion_of_control.context.main import dependencies_test_main


def test_dependencies():
    assert dependencies_test_main() == "Postgre respoistory"
