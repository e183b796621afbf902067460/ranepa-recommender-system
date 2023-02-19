from instacart.interfaces.fabrics.interface import iFabric


class InstaCartBridgeConfigurator:

    def __init__(self, abstract, fabric_name: str, handler_name: str) -> None:
        self._abstract = abstract
        self._fabric_name = fabric_name
        self._handler_name = handler_name

    @property
    def abstract(self):
        return self._abstract

    def produce_fabric(self) -> iFabric:
        return self.abstract.get_fabric(self._fabric_name)

    def produce_handler(self):
        return self.produce_fabric().get_handler(self._handler_name)
