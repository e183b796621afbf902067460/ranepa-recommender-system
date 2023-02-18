from abc import ABC
from typing import final

from instacart.interfaces.fabrics.interface import iFabric

from instacart.fabrics.models.classifiers.fabric import classifiersModelsFabric


class InstaCartModelsAbstractFabric(ABC):

    def __init__(self) -> None:
        self._fabrics: dict = dict()

    @final
    def add_fabric(self, fabric_name: str, fabric: iFabric) -> None:
        if not self._fabrics.get(fabric_name):
            self._fabrics[fabric_name] = fabric

    @final
    def get_fabric(self, fabric_name: str) -> iFabric:
        fabric: iFabric = self._fabrics.get(fabric_name)
        if not fabric:
            raise ValueError(f'Set Fabric for {fabric_name} fabric type')
        return fabric


instaCartModelsAbstractFabric = InstaCartModelsAbstractFabric()

instaCartModelsAbstractFabric.add_fabric(fabric_name=classifiersModelsFabric.name(), fabric=classifiersModelsFabric)
