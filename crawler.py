from decimal import Decimal

import scrapy


class BNRSpider(scrapy.Spider):
    name = "bnr_spider"
    start_urls = ['https://www.bnr.ro/Cursul-de-schimb-524.aspx']

    def parse(self, response, **kwargs):
        curs_table = response.css('.cursTable tbody tr')
        for moneda in curs_table:
            value = float(moneda.css('td::text')[6].get().replace(",", "."))
            name = moneda.css('.c2::text').get()
            yield {
                name: value
            }
