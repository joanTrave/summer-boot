from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def custom_method(self) -> str:
        raise NotImplementedError
