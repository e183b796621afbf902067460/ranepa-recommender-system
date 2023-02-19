import os
import pandas as pd
from functools import lru_cache

from instacart.dto.products.dto import ProductsDto
from instacart.dto.transactions.dto import TransactionsDto


NTAIL = os.getenv('NTAIL', 10)


class MixedProductsAndTransactionsDto(object):

    PRODUCT_ID = 'product_id'
    USER_ID = 'user_id'

    def __init__(self, products: ProductsDto, transactions: TransactionsDto) -> None:
        self._products, self._transactions = products, transactions

    @property
    def products_dto(self):
        return self._products

    @property
    def transactions_dto(self):
        return self._transactions

    @property
    def products_filtered_df(self):
        return self.products_dto.filtered_df

    @property
    def transactions_filtered_df(self):
        return self.transactions_dto.filtered_df

    def _merge_filtered_df(self, on: str = PRODUCT_ID, how: str = 'left') -> pd.DataFrame:
        return self.transactions_filtered_df.merge(self.products_filtered_df, on=on, how=how)

    @property
    @lru_cache
    def df(self) -> pd.DataFrame:
        return self._merge_filtered_df().groupby([self.USER_ID, self.PRODUCT_ID]).tail(NTAIL)
