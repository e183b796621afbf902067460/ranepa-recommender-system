
# InstaCart Recommender System

No local dependencies.

---
InstaCart Recommender System is an ML-framework that helps to train certain ML-model based on InstaCart's transactions data and make some recommendations for our users. The scalability of the framework is based on it's architecture that provides a simple way to scale up amount of a new handlers and add it to right factories. Each factory is an independent ML-unit and must located at abstract factory. Bridge helps to orchestrate of whole amount of factories and handlers.

# Usage
For example, to get [`InstaCartCatBoostClassifier`](https://github.com/e183b796621afbf902067460/ranepa-recommender-system/blob/master/instacart/handlers/models/catboost/model.py#L15) need to call [`InstaCartBridgeConfigurator`](https://github.com/e183b796621afbf902067460/ranepa-recommender-system/blob/master/instacart/bridge/bridge.py#L4) and pass to it constructor next arguments and then call `produce_handler()` method:

```python
from instacart.bridge.bridge import InstaCartBridgeConfigurator
from instacart.abstracts.models.abc import instaCartModelsAbstractFabric
from instacart.fabrics.models.fabric import ModelsFabric
from instacart.handlers.models.catboost.model import InstaCartCatBoostClassifier


model_class = InstaCartBridgeConfigurator(
    abstract=instaCartModelsAbstractFabric,
    fabric_name=ModelsFabric.name(),
    handler_name=InstaCartCatBoostClassifier.name()
).produce_handler()
```

But, to initialize produced model we should load transactions data to specific classes to store the data:

```python
from instacart.dto.products.dto import ProductsDto
from instacart.dto.transactions.dto import TransactionsDto
from instacart.dto.mixed.dto import MixedProductsAndTransactionsDto


PRODUCTS_CSV_PATH = '<path to products.csv>'
TRANSACTIONS_CSV_PATH = '<path to transactions.csv>'
SUBMIT_PATH = '<path for submit.csv>'


products = ProductsDto(csv_file_path=PRODUCTS_CSV_PATH)
transactions = TransactionsDto(csv_file_path=TRANSACTIONS_CSV_PATH)
mix = MixedProductsAndTransactionsDto(products=products, transactions=transactions)
```

And after that initialize the model:

```python
model = model_class(mix=mix)
```

Model class have two-overloaded methods that helps to train model and make predictions in such easier way than you thought:

```python
model.instacart_train()
model.instacart_predict(is_save_to_csv=True, csv_path=SUBMIT_PATH)
```

After that, we have `recommendations.csv` file that store top-10 recommendations for each user.

