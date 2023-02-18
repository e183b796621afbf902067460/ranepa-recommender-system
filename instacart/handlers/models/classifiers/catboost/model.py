from typing import Type

from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

from instacart.decorators.camel2snake import camel2snake
from instacart.dto.mixed.dto import MixedProductsAndTransactionsDto
from instacart.bridge.bridge import InstaCartBridgeConfigurator
from instacart.abstracts._features.abc import _instaCartFeaturesAbstractFabric, _InstaCartFeaturesAbstractFabric
from instacart.fabrics.features.classifiers.catboost.fabric import catBoostClassifierFeaturesFabric, CatBoostClassifierFeaturesFabric
from instacart.handlers.features.classifiers.catboost.main.feature import MainFeature


def apk(actual, predicted, k=10):
    if len(predicted) > k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0

    for i, p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)

    return score / min(len(actual), k)


def mapk(actual, predicted, k=10):
    return np.mean([apk(a, p, k) for a, p in zip(actual, predicted)])


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
                df = df.merge(feature_df, how='left', on=['user_id', 'product_id'])
        return df

    def instacart_train(self) -> None:
        df = self._prepare_df()
        x = df.drop(columns=MainFeature.name()).values
        y = df[MainFeature.name()].values
        _x, X, _y, Y = train_test_split(x, y, test_size=.01, stratify=y)
        self.fit(_x, _y)

        y = self.predict(X)
        print(f'map@10: {mapk(actual=[y], predicted=[Y])}')







