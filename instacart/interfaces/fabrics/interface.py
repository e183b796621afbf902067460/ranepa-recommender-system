from abc import ABC, abstractmethod


class iFabric(ABC):

    def __init__(self) -> None:
        self._handlers: dict = dict()

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError(f'Set {self.name.__name__} attribute for {self.__class__.__name__}')

    @property
    def handlers(self) -> dict:
        return self._handlers

    @abstractmethod
    def add_handler(self, *args, **kwargs) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.add_handler.__name__}() implementation")

    @abstractmethod
    def get_handler(self, *args, **kwargs) -> object:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have a {self.get_handler.__name__}() implementation")