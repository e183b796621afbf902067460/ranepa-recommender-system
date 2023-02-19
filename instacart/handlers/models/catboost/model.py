from typing import Type

from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

from instacart.decorators.camel2snake import camel2snake
from instacart.dto.mixed.dto import MixedProductsAndTransactionsDto
from instacart.bridge.bridge import InstaCartBridgeConfigurator
from instacart.abstracts._features.abc import _instaCartFeaturesAbstractFabric, _InstaCartFeaturesAbstractFabric
from instacart.fabrics.features.catboost.fabric import catBoostClassifierFeaturesFabric, CatBoostClassifierFeaturesFabric
from instacart.handlers.features.catboost.main.feature import MainFeature


class InstaCartCatBoostClassifier(CatBoostClassifier):

    @classmethod
    @camel2snake
    def name(cls):
        return __class__.__name__

    @property
    def mix(self) -> MixedProductsAndTransactionsDto:
        return self._mix

    def __init__(self, mix: MixedProductsAndTransactionsDto, *args, **kwargs) -> None:
        CatBoostClassifier.__init__(self, *args, **kwargs)
        self._mix = mix

        self.__recommendations = None
        self.__prepared_df = None

    def _prepare_df(
            self,
            bridge: Type[InstaCartBridgeConfigurator] = InstaCartBridgeConfigurator,
            features_abc: _InstaCartFeaturesAbstractFabric = _instaCartFeaturesAbstractFabric,
            features_fabric: CatBoostClassifierFeaturesFabric = catBoostClassifierFeaturesFabric
    ) -> pd.DataFrame:
        futures = list()
        for feature_name, _ in features_fabric.handlers.items():
            feature_class = bridge(
                abstract=features_abc,
                fabric_name=features_fabric.name(),
                handler_name=feature_name
            ).produce_handler()
            feature = feature_class(mix=self.mix)
            futures.append(feature.prepare_df())
        df = pd.DataFrame()
        for future in futures:
            feature_df: pd.DataFrame = future.result()
            if df.empty:
                df = feature_df
            else:
                df = df.merge(feature_df, how='left', on=[self.mix.USER_ID, self.mix.PRODUCT_ID])
        return df

    def instacart_train(self) -> None:
        self.__prepared_df = self._prepare_df()
        x = self.__prepared_df.drop(columns=MainFeature.name()).values
        y = self.__prepared_df[MainFeature.name()].values
        _x, X, _y, Y = train_test_split(x, y, test_size=.01, stratify=y)
        self.fit(_x, _y)

    def instacart_predict(self, is_save_to_csv: bool = False):
        df = self.__prepared_df.drop(columns=MainFeature.name())
        self.__recommendations = self.predict_proba(df.values)
        self.__recommendations = pd.concat(
            [
                df[[self.mix.USER_ID, self.mix.PRODUCT_ID]],
                pd.Series(self.__recommendations[:, 1], name='proba')
            ],
            axis=1
        ).sort_values(by=['user_id', 'proba'], ascending=[True, False])
        if is_save_to_csv:
            df = self.__recommendations.groupby(['user_id'], as_index=False).head(10)
            output = df.groupby(['user_id'], as_index=False).agg(lambda product_ids: ' '.join(str(value) for value in list(product_ids)))[['user_id', 'product_id']]
            output.to_csv('recommendations.csv', index=False)
