import scrapy,os
from scrapy.crawler import CrawlerProcess
from dota_nn.spiders.spiders import MatchIDSpider
from scrapy.exporters import JsonItemExporter
from scrapy.utils.project import get_project_settings
from conv_data import DataConverter

if __name__ == "__main__":
    directory = os.path.join(os.path.abspath(os.curdir),'data')
    params_dir = os.path.join(os.path.abspath(os.curdir),"data_params")
    setting = get_project_settings()
    process = CrawlerProcess(get_project_settings())
    process.crawl(MatchIDSpider)
    process.start()
    converter = DataConverter(directory,params_dir)
    converter.get_matches()