import abc
import datetime
import typing

import pandas


class DataSource:

    @abc.abstractmethod
    def fetch_prices(self, symbols: typing.Set[str], start: datetime.date, end: datetime.date) -> pandas.DataFrame:
        return None

    @abc.abstractmethod
    def is_closeable(self) -> bool:
        """
        Return whether or not the markat has closing hours.
        Cryptocurrencies for examples does not.
        """
        
        return True
