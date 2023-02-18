from instacart.bridge.bridge import InstaCartBridgeConfigurator
from instacart.abstracts.models.abc import instaCartModelsAbstractFabric
from instacart.fabrics.models.classifiers.fabric import ClassifiersModelsFabric
from instacart.handlers.models.classifiers.catboost.model import InstaCartCatBoostClassifier

from instacart.dto.products.dto import ProductsDto
from instacart.dto.transactions.dto import TransactionsDto
from instacart.dto.mixed.dto import MixedProductsAndTransactionsDto


products = ProductsDto(csv_file_path='products.csv')
transactions = TransactionsDto(csv_file_path='transactions.csv')
mix = MixedProductsAndTransactionsDto(products=products, transactions=transactions)

model_class = InstaCartBridgeConfigurator(
    abstract=instaCartModelsAbstractFabric,
    fabric_name=ClassifiersModelsFabric.name(),
    handler_name=InstaCartCatBoostClassifier.name()
).produce_handler()
model = model_class(mix=mix)

model.instacart_train()
