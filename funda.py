from funda_scraper import FundaScraper
from model import House
from interface import RentProviderInterface

class Funda(RentProviderInterface):
    def __init__(self, city='amsterdam', price=[0,9000], header={}):
        super().__init__(city, price)

        self._scraper = FundaScraper(city, want_to='rent', find_past=False)
        self._url_pattern = 'https://www.funda.nl/huur/%s/%s-%s-%s/'

    def Run(self):
        df = self._scraper.run()
        ret = []
        for idx, row in df.iterrows():
            if not self._isPriceMatched(int(row['price'])):
                continue
            url = self._url_pattern % (row['city'], row['house_type'], row['house_id'], row['address'].replace(' ', '-'))
            ret.append(House(row['house_id'], url, row['address'], int(row['price']), str(row['living_area'])+' m²'))
        return ret

