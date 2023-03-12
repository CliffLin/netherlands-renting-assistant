
class RentProviderInterface:
    def __init__(self, city, price):
        self._min_price = price[0]
        self._max_price = price[1]
        self._city = city

    def _isPriceMatched(self, price):
        if price >= self._min_price and price <= self._max_price:
            return True
        return False

    def Run(self):
        pass
