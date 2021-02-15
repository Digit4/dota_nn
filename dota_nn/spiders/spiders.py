import json
from os.path import join as make_path

import scrapy
from scrapy import Request
from dota_nn import settings

class MatchIDSpider(scrapy.Spider):
    name = "match_id"
    download_delay = 2

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        }
    }

    start_urls = [
        "https://www.dotabuff.com/matches?game_mode=all_pick"
    ]

    def parse(self, response, **kwargs):
        opendota_url = 'https://api.opendota.com/api/matches/'
        match_ids = [x.get() for x in response.selector.xpath("//tr/td/a[contains(@href,'/matches/')]/text()") if x.get().isnumeric()]
        for mid in match_ids:
            match_url = opendota_url + mid
            # print(match_url)
            yield Request(match_url,callback=self.parse_opendota)
            # yield {"match_id":mid}

    def store_opendota_json(self,data):
        filename = str(data['match_id']) + '.json'
        full_path = make_path(make_path(settings.PROJECT_ROOT,'data'),filename)
        with open(full_path,'w+') as f:
            f.write(json.dumps(data))

    def parse_opendota(self, response, ** kwargs):
        json_string = response.json()
        self.store_opendota_json(json_string)
        return json_string
