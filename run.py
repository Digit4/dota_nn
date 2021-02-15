import scrapy
from scrapy.crawler import CrawlerProcess
from dota_nn.spiders.spiders import MatchIDSpider
from scrapy.exporters import JsonItemExporter
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":
    setting = get_project_settings()
    process = CrawlerProcess(get_project_settings())
    process.crawl(MatchIDSpider)
    process.start()