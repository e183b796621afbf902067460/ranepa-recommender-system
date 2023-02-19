from instacart.interfaces.fabrics.interface import iFabric
from instacart.decorators.camel2snake import camel2snake

from instacart.handlers.models.catboost.model import InstaCartCatBoostClassifier


class ClassifiersModelsFabric(iFabric):

    @classmethod
    @camel2snake
    def name(cls) -> str:
        return __class__.__name__

    def add_handler(self, name: str, handler) -> None:
        if not self._handlers.get(name):
            self._handlers[name] = handler

    def get_handler(self, name: str):
        handler = self._handlers.get(name)
        if not handler:
            raise ValueError(f'Set {__class__.__name__} handler for {name}')
        return handler


classifiersModelsFabric = ClassifiersModelsFabric()

classifiersModelsFabric.add_handler(name=InstaCartCatBoostClassifier.name(), handler=InstaCartCatBoostClassifier)
