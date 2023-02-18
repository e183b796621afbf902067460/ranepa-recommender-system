from abc import ABC, abstractmethod
import pandas as pd

from instacart.dto.mixed.dto import MixedProductsAndTransactionsDto


class iFeature(ABC):

    def __init__(self, mix: MixedProductsAndTransactionsDto):
        self._mix = mix

    @property
    def mix(self) -> MixedProductsAndTransactionsDto:
        return self._mix

    @property
    def index(self):
        return self.mix.df.set_index([self.mix.USER_ID, self.mix.PRODUCT_ID]).index.drop_duplicates()

    @abstractmethod
    def prepare_df(self) ->pd.DataFrame:
        raise NotImplementedError(f'{self.prepare_df.__name__}() function is not implemented in {__class__.__name__}')

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError(f'{self.name.__name__} attribute is not set in {__class__.__name__}')

