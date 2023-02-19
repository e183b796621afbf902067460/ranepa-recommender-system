from instacart.bridge.bridge import InstaCartBridgeConfigurator
from instacart.abstracts.models.abc import instaCartModelsAbstractFabric
from instacart.fabrics.models.fabric import ModelsFabric
from instacart.handlers.models.catboost.model import InstaCartCatBoostClassifier

from instacart.dto.products.dto import ProductsDto
from instacart.dto.transactions.dto import TransactionsDto
from instacart.dto.mixed.dto import MixedProductsAndTransactionsDto


PRODUCTS_CSV_PATH = '/home/user/repositories/defi-notebooks/products.csv'
TRANSACTIONS_CSV_PATH = '/home/user/repositories/defi-notebooks/transactions.csv'


products = ProductsDto(csv_file_path=PRODUCTS_CSV_PATH)
transactions = TransactionsDto(csv_file_path=TRANSACTIONS_CSV_PATH)
mix = MixedProductsAndTransactionsDto(products=products, transactions=transactions)

model_class = InstaCartBridgeConfigurator(
    abstract=instaCartModelsAbstractFabric,
    fabric_name=ModelsFabric.name(),
    handler_name=InstaCartCatBoostClassifier.name()
).produce_handler()
model = model_class(mix=mix)

model.instacart_train()
model.instacart_predict()
