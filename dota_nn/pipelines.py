# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging


class DotaNnPipeline:
    def process_item(self, item, spider):
        return item
    def open_spider(self,spider):
        print('Spider Started running')
    def close_spider(self, spider):
        print("Spider completed process")

class MatchIDPipeline:
    def process_match_id(self, match_id, spider):
        return match_id
    def open_spider(self,spider):
        print('Spider Started running in MatchID Pipeline')
    def close_spider(self, spider):
        print("Spider completed process in MatchID Pipeline")

