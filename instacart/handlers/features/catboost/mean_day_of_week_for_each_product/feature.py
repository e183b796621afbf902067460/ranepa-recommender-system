import pandas as pd

import instacart.upd.sqldf.upd as psql
from instacart.interfaces.features.interface import iFeature
from instacart.decorators.camel2snake import camel2snake
from instacart.decorators.threadmethod import threadmethod


pysqldf = lambda q: psql.sqldf(q, globals())


class MeanDayOfWeekForEachProduct(iFeature):
    """
    Ср-нее значение order_dow, сгруппированное по product_id
    """
    @classmethod
    @camel2snake
    def name(cls) -> str:
        return __class__.__name__

    @threadmethod
    def prepare_df(self, *args, **kwargs) -> pd.DataFrame:
        globals()['df'] = self.mix.df
        return pysqldf(
            f'''
                SELECT
                    product_id,
                    AVG(order_dow) AS {self.name()}
                FROM
                    df
                GROUP BY
                    product_id
            '''
        )

