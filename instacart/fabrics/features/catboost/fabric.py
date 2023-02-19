from instacart.interfaces.fabrics.interface import iFabric
from instacart.decorators.camel2snake import camel2snake

from instacart.handlers.features.catboost.all_products_count_for_each_user_and_product.feature import AllProductsCountForEachUserAndProductFeature
from instacart.handlers.features.catboost.all_reordered_count_for_each_user_and_product.feature import AllReorderedCountForEachUserAndProductFeature
from instacart.handlers.features.catboost.main.feature import MainFeature
from instacart.handlers.features.catboost.mean_day_of_week_for_each_user_and_product.feature import MeanDayOfWeekForEachUserAndProduct
from instacart.handlers.features.catboost.mean_days_since_prior_order_for_each_user_and_product.feature import MeanDaysSincePriorOrderForEachUserAndProduct
from instacart.handlers.features.catboost.mean_hour_of_day_for_each_user_and_product.feature import MeanHourOfDayForEachUserAndProduct


class CatBoostClassifierFeaturesFabric(iFabric):

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


catBoostClassifierFeaturesFabric = CatBoostClassifierFeaturesFabric()

catBoostClassifierFeaturesFabric.add_handler(name=AllProductsCountForEachUserAndProductFeature.name(), handler=AllProductsCountForEachUserAndProductFeature)
catBoostClassifierFeaturesFabric.add_handler(name=AllReorderedCountForEachUserAndProductFeature.name(), handler=AllReorderedCountForEachUserAndProductFeature)
catBoostClassifierFeaturesFabric.add_handler(name=MainFeature.name(), handler=MainFeature)
catBoostClassifierFeaturesFabric.add_handler(name=MeanDayOfWeekForEachUserAndProduct.name(), handler=MeanDayOfWeekForEachUserAndProduct)
catBoostClassifierFeaturesFabric.add_handler(name=MeanDaysSincePriorOrderForEachUserAndProduct.name(), handler=MeanDaysSincePriorOrderForEachUserAndProduct)
catBoostClassifierFeaturesFabric.add_handler(name=MeanHourOfDayForEachUserAndProduct.name(), handler=MeanHourOfDayForEachUserAndProduct)
