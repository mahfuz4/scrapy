from os import link

import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a").getall()
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            absolute_url = f"https://www.worldometers.info{link}"
            yield scrapy.Request(url= absolute_url)
