import pandas as pd

import instacart.upd.sqldf.upd as psql
from instacart.interfaces.features.interface import iFeature
from instacart.decorators.camel2snake import camel2snake
from instacart.decorators.threadmethod import threadmethod


pysqldf = lambda q: psql.sqldf(q, globals())


class AllReorderedCountForEachProductFeature(iFeature):
    """
    Кол-во reordered, сгруппированные по product_id
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
                    SUM(reordered) AS {self.name()}
                FROM
                    df
                GROUP BY
                    product_id
            '''
        )

