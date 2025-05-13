import scrapy

# 实现一个Spider，必须提供三个属性：name、 start_requests Spider启动时爬取的URL列表、 parse()回调函数
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls=[
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as file:
            file.write(response.body)
        self.log('save file %s' % filename)