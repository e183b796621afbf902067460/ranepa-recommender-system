import pandas as pd

import instacart.upd.sqldf.upd as psql
from instacart.interfaces.features.interface import iFeature
from instacart.decorators.camel2snake import camel2snake
from instacart.decorators.threadmethod import threadmethod


pysqldf = lambda q: psql.sqldf(q, globals())


class AllReorderedCountForEachUserAndProductFeature(iFeature):
    """
    Кол-во reordered, сгруппированные по user_id и product_id
    """
    @classmethod
    @camel2snake
    def name(cls) -> str:
        return __class__.__name__

    @threadmethod
    def prepare_df(self, *args, **kwargs) -> pd.DataFrame:
        return self.mix.df.groupby([self.mix.USER_ID, self.mix.PRODUCT_ID], as_index=False).agg(sum=('reordered', 'sum')).rename(columns={'sum': self.name()})

