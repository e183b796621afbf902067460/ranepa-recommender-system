import pandas as pd

import instacart.upd.sqldf.upd as psql
from instacart.interfaces.features.interface import iFeature
from instacart.decorators.camel2snake import camel2snake
from instacart.decorators.threadmethod import threadmethod


pysqldf = lambda q: psql.sqldf(q, globals())


class MainFeature(iFeature):

    @classmethod
    @camel2snake
    def name(cls) -> str:
        return __class__.__name__

    @threadmethod
    def prepare_df(self, *args, **kwargs) -> pd.DataFrame:
        globals()['df'] = self.mix.df
        globals()['last_order_id_for_each_user_df'] = pysqldf(
            '''
               SELECT
                   max(order_number) AS order_number,
                   order_id
                FROM 
                    df
                GROUP BY
                    user_id
            '''
        )
        last_transaction_for_each_user_df = pysqldf(
            '''
                SELECT
                    *
                FROM
                    df
                WHERE
                    order_id IN (
                        SELECT
                            order_id
                        FROM 
                            last_order_id_for_each_user_df
                    )
            '''
        )
        return last_transaction_for_each_user_df \
            .groupby([self.mix.USER_ID, self.mix.PRODUCT_ID], sort=False) \
            .size() \
            .astype('uint8') \
            .to_frame(self.name()) \
            .reindex(self.index, fill_value=0)

