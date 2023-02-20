import pandas as pd

import instacart.upd.sqldf.upd as psql
from instacart.interfaces.features.interface import iFeature
from instacart.decorators.camel2snake import camel2snake
from instacart.decorators.threadmethod import threadmethod


pysqldf = lambda q: psql.sqldf(q, globals())


class MeanDayOfWeekForEachUserAndProduct(iFeature):
    """
    Ср-нее значение order_dow, сгруппированное по user_id и product_id
    """
    @classmethod
    @camel2snake
    def name(cls) -> str:
        return __class__.__name__

    @threadmethod
    def prepare_df(self, *args, **kwargs) -> pd.DataFrame:
        return self.mix.df.groupby([self.mix.USER_ID, self.mix.PRODUCT_ID], as_index=False).agg(mean=('order_dow', 'mean')).rename(columns={'mean': self.name()})

