import scrapy

# 实现一个Spider，必须提供三个属性：name、 start_requests Spider启动时爬取的URL列表、 parse()回调函数
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls=[
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        print(f'西瓜皮：meet {response.url}')
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }
        # 写入response到本地文件
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as file:
            # file.write(response.body)
        # self.log('save file %s' % filename)

        # 分页需要跟进链接到下一页,得到这个 /page/2/
        next_page=response.css('li.next a::attr(href)').extract_first()
        if(next_page is not None):
            # 查看response的url：response.url
            # 相对路径替换到绝对路径的正确位置上可以使用urljoin方法
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
