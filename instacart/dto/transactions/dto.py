import pandas as pd

from instacart.interfaces.dto.interface import iDto


class TransactionsDto(iDto):
    PRODUCT_ID = 'product_id'
    ORDER_ID = 'order_id'
    USER_ID = 'user_id'
    ORDER_NUMBER = 'order_number'
    ORDER_DOW = 'order_dow'
    ORDER_HOUR_OF_DAY = 'order_hour_of_day'
    DAYS_SINCE_PRIOR_ORDER = 'days_since_prior_order'
    ADD_TO_CART_ORDER = 'add_to_cart_order'
    REORDERED = 'reordered'

    _FILTER_COLUMNS = [
        PRODUCT_ID,
        ORDER_ID,
        USER_ID,
        ORDER_NUMBER,
        ORDER_DOW,
        ORDER_HOUR_OF_DAY,
        DAYS_SINCE_PRIOR_ORDER,
        ADD_TO_CART_ORDER,
        REORDERED
    ]
