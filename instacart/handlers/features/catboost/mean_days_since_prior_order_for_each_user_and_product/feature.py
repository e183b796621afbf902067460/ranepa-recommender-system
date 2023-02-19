import pandas as pd

import instacart.upd.sqldf.upd as psql
from instacart.interfaces.features.interface import iFeature
from instacart.decorators.camel2snake import camel2snake
from instacart.decorators.threadmethod import threadmethod


pysqldf = lambda q: psql.sqldf(q, globals())


class MeanDaysSincePriorOrderForEachUserAndProduct(iFeature):
    """
    Ср-нее значение days_since_prior_order, сгруппированное по user_id и product_id
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
                    user_id,
                    product_id,
                    AVG(days_since_prior_order) AS {self.name()}
                FROM
                    df
                GROUP BY
                    user_id,
                    product_id
            '''
        )

