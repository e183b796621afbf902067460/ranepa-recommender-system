from abc import ABC
import os
from typing import List
import pandas as pd

from instacart.upd.memreduce.upd import reduce_mem_usage


NROWS = os.getenv('NROWS', None)


class iDto(ABC):
    _FILTER_COLUMNS: List[str] = None

    def __init__(self, csv_file_path: str) -> None:
        self._raw_df: pd.DataFrame = reduce_mem_usage(pd.read_csv(csv_file_path) if not NROWS else pd.read_csv(csv_file_path, nrows=NROWS))
        self._raw_df.info()
        self._filtered_df: pd.DataFrame = self._raw_df[self._FILTER_COLUMNS]

    @property
    def raw_df(self):
        return self._raw_df

    @property
    def filtered_df(self):
        return self._filtered_df
