# summer-boot #
After spring it comes the summer.

## Installation ##
```bash
pip install python-summer-boot
```

## Inversion of control ##
summer-boot provides an easy dependency injection by splitting classes between services and injectors.
A service is a dependency and an injector is a class that consumes dependencies.

You can discover services with the ```disvover_services``` function.
It is recommended to create a setup file located in your sources root and call discover services function there, once. 
Here you have an example:
```python
import os

from summer.inversion_of_control.service_locator import get_executable_parent_path, discover_services

executable_parent_path = get_executable_parent_path(os.getcwd())


def setup():
    discover_services(executable_parent_path)
```
**⚠️ Remember to call setup function before use any injection. ⚠️**

You can define services using the ```@service``` decorator at class level.
```python
from summer.inversion_of_control.dependencies import service

from src.mock_entity.core.i_repository import IRepository


@service()
class PostgreRepository(IRepository):
    def custom_method(self):
        return "Postgre repository"
```
Here the code of ```IRepository```:
```python
from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def custom_method(self) -> str:
        raise NotImplementedError
```
Finally, you can consume injected dependencies with the ```@autowired``` decorator, upside the function that needs 
dependencies. In most of the cases it will be the ```__init__``` function:
```python
from summer.inversion_of_control.dependencies import autowired

from src.mock_entity.core.i_repository import IRepository


class UseCase:
    @autowired
    def __init__(self, repository: IRepository):
        self.repository = repository

    def my_use_case(self) -> str:
        return self.repository.custom_method()
```

## Models ##
**⚠️ It is necessary to install pydantic in order to use this module. ⚠️**

SummerBoot implements some models using inheritance from pydantic.

### CamelModel ###

A model which every attribute is represented as camelCase perhaps is coded as snake_case. I.e.:
```python
from summer.models.camel.camel_model import CamelModel


class MockCamelModel(CamelModel):
    mock_attribute: str = "mock"
```