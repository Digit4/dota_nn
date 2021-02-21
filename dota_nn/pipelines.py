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
    def process_item(self, match_id, spider):
        self.prev_scraped_file.write(str(match_id['match_id'])+'\n')
        logging.info(match_id['match_id'])
        return match_id
    def open_spider(self,spider):
        self.prev_scraped_file = open('prev_scraped.csv','w')
    def close_spider(self, spider):
        self.prev_scraped_file.close()

