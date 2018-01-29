import scrapy
from scrapy.loader import ItemLoader
from CORDIS.items import CordisItem

class CordisSpider(scrapy.Spider):
    name = 'cordis'
    allowed_domains = ['cordis.europa.eu']
    start_urls = ['http://cordis.europa.eu/project/rcn/%d_en.html' %(n) for n in range(210216, 210217)]

    def parse(self, response):
        # Misconfiguration to check - eu in response.xpath not needed
        #for eu in response.xpath('//*[@id="container-pack"]'):
            item = CordisItem()
            item['Meta'] = response.xpath('/html/head/meta[23]').extract()
            item['Project_ACR'] = response.xpath('//*[@id="dynamiccontent"]/div[1]/h1/text()').extract()
            item['Project_Title'] = response.xpath('//*[@id="dynamiccontent"]/h2/text()').extract()
            item['Total_Cost'] = response.xpath('//*[@id="dynamiccontent"]/div[3]/div/div[1]/div[1]/text()').extract()
            item['EU_Contribution'] = response.xpath('//*[@id="dynamiccontent"]/div[3]/div/div[1]/div[2]/text()').extract()
            item['Coordinated_in'] = response.xpath('//*[@id="dynamiccontent"]/div[3]/div/div[1]/div[3]/text()').extract()
            item['Topic_s'] = response.xpath('//*[@id="dynamiccontent"]/div[3]/div/div[2]/div[1]/a/text()').extract()
            item['Call_for_Proposal'] = response.xpath('//*[@id="dynamiccontent"]/div[3]/div/div[2]/div[2]/text()').extract()
            item['Funding_scheme'] = response.xpath('//*[@id="dynamiccontent"]/div[3]/div/div[2]/div[3]/text()').extract()
            item['Project_ID'] = map(unicode.strip, response.xpath('.//*[@id="dynamiccontent"]/div[1]/text()').re('[.0-9]+'))
            item['To'] = response.xpath('normalize-space(.//*[@id="dynamiccontent"]/div[2]/text()[3])').extract()
            item['From'] = response.xpath('normalize-space(.//*[@id="dynamiccontent"]/div[2]/text()[2])').extract()
            item['Partners'] = response.css('.name').xpath('text()').extract()
            item['Country'] = response.css('.country').xpath('text()').extract()
            item['Activity'] = response.css('.contact').xpath('text()').extract()

        #for eu in response.css('div.objective'):
            item['Technology_Description'] = response.css('p::text').extract_first()
            yield item
"""
    def parse(self, response):
        l = ItemLoader(item=CordisItem(), response=response)
        l.add_xpath('Project_ACR', '//*[@id="dynamiccontent"]/div[1]/h1/text()')
        l.add_xpath('Project_Title', '//*[@id="dynamiccontent"]/h2/text()')
        l.add_xpath('Total_Cost', '//*[@id="dynamiccontent"]/div[3]/div/div[1]/div[1]/text()')
        l.add_xpath('EU_Contribution', '//*[@id="dynamiccontent"]/div[3]/div/div[1]/div[2]/text()')
        l.add_xpath('Coordinated_in', '//*[@id="dynamiccontent"]/div[3]/div/div[1]/div[3]/text()')
        l.add_xpath('Topic_s', '//*[@id="dynamiccontent"]/div[3]/div/div[2]/div[1]/a/text()')
        l.add_xpath('Call_for_Proposal', '//*[@id="dynamiccontent"]/div[3]/div/div[2]/div[2]/text()')
        l.add_xpath('Funding_scheme', '//*[@id="dynamiccontent"]/div[3]/div/div[2]/div[3]/text()')
        #l.add_xpath('Project_ID', '//*[@id="dynamiccontent"]/div[1]/text()'.re('[.0-9]+')')  map(unicode.strip, response.xpath('.//*[@id="dynamiccontent"]/div[1]/text()').re('[.0-9]+'))
        l.add_xpath('To', 'normalize-space(.//*[@id="dynamiccontent"]/div[2]/text()[3])')
        l.add_xpath('From', 'normalize-space(.//*[@id="dynamiccontent"]/div[2]/text()[2])')
        #l.add_xpath('Partners', 'response.css('.name').xpath('text()')')
        #l.add_xpath('Country', 'response.css('.country').xpath('text()')')
        #l.add_xpath('Activity', 'response.css('.contact').xpath('text()')')
        l.add_css('Technology_Description', 'p::text') # error extract all p

        return l.load_item()
"""
