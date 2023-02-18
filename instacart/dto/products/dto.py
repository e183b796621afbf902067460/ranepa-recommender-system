import pandas as pd

from instacart.interfaces.dto.interface import iDto


class ProductsDto(iDto):
    PRODUCT_ID = 'product_id'
    AISLE_ID = 'aisle_id'
    DEPARTMENT_ID = 'department_id'

    _FILTER_COLUMNS = [
        PRODUCT_ID,
        AISLE_ID,
        DEPARTMENT_ID
    ]
