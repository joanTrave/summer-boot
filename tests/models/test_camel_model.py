import json

from summer.models.camel.camel_model import CamelModel


class MockCamelModel(CamelModel):
    mock_attribute: str = "mock"


def test_camel_model():
    assert json.loads(MockCamelModel().json(by_alias=True)) == {"mockAttribute": "mock"}
