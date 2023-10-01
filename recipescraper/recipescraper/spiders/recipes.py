import scrapy


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    allowed_domains = ["www.marmiton.org"]
    start_urls = ["https://www.marmiton.org"]

    def parse(self, response):
        pass
