from decimal import Decimal

import scrapy
import json

class BNRSpider(scrapy.Spider):
    name = "bnr_spider"
    start_urls = ['https://www.bnr.ro/Cursul-de-schimb-524.aspx']

    def parse(self, response, **kwargs):
        data = dict()
        data["RON"] = 1
        curs_table = response.css('.cursTable tbody tr')
        for moneda in curs_table:
            value = float(moneda.css('td::text')[6].get().replace(",", "."))
            name = moneda.css('.c2::text').get()
            data[name] = value

        with open('output.json', 'w') as fp:
            json.dump(data, fp)
