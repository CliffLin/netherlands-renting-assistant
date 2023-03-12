import pararius
from model import House
from interface import RentProviderInterface

class Pararius(RentProviderInterface):
    def __init__(self, city='amsterdam', price=[0,9000], header={}):
        super().__init__(city, price)
        self._min_price = price[0]
        self._max_price = price[1]
        self._header = header

    def Run(self):
        data = pararius.fetchData(self._city, self._min_price, self._max_price, header=self._header)
        ret = []
        for row in data:
            ret.append(
                House(
                    row[7], row[7], row[6], row[2], row[3]
                )
            )
        return ret
