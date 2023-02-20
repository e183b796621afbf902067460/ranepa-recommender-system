from abc import ABC

from instacart.interfaces.fabrics.interface import iFabric
from instacart.fabrics.models.fabric import modelsFabric


class InstaCartModelsAbstractFabric(ABC):

    def __init__(self) -> None:
        self._fabrics: dict = dict()

    def add_fabric(self, fabric_name: str, fabric: iFabric) -> None:
        if not self._fabrics.get(fabric_name):
            self._fabrics[fabric_name] = fabric

    def get_fabric(self, fabric_name: str) -> iFabric:
        fabric: iFabric = self._fabrics.get(fabric_name)
        if not fabric:
            raise ValueError(f'Set Fabric for {fabric_name} fabric type')
        return fabric


instaCartModelsAbstractFabric = InstaCartModelsAbstractFabric()

instaCartModelsAbstractFabric.add_fabric(fabric_name=modelsFabric.name(), fabric=modelsFabric)
