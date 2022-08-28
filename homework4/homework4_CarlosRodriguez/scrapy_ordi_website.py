# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 2022
@author: Carlos Rodriguez
scrapy runspider -o ./scrap.json scrapy_ordi_website.py
references consulted https://www.scraperapi.com/blog/css-selectors-cheat-sheet/
"""
import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    #a list of URLs that you start to crawl from. We'll start with one URL.
    url = "https://ordi.eu/sulearvutid?___store=en&___from_store=et"
    headers =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
            }

    def start_requests(self):
        # Set the headers here.
        yield scrapy.http.Request(self.url, headers=self.headers)

    def parse(self, response):
        """
        We’ll use CSS selectors for now since CSS is the easier option and a
        perfect fit for finding all the sets on the page. If you look at the
        HTML for the page, you'll see that each set is specified with the
        class set. Since we're looking for a class, we'd use .set for our
        CSS selector. All we have to do is pass that selector into the
        response object
        """
        SET_SELECTOR = '.item'
        for brickset in response.css(SET_SELECTOR):
            """The brickset object we’re looping over has its own css method, 
            so we can pass in a selector to locate child elements
            """
            TITLE = 'h2 ::text'
            PRICE = '.price ::text'
            PICTURE_HREF = 'img ::attr(src)'

            yield {
                'Title': brickset.css(TITLE).extract_first(),
                'Price': brickset.css(PRICE).extract_first(),
                'Picture href': brickset.css(PICTURE_HREF).extract_first(),
            }
        # define a selector for the "next page" link
        NEXT_PAGE_SELECTOR = 'a.next ::attr(href)'

        # extract the first match, and check if it exists
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

        if next_page:
             url = response.urljoin(next_page)
             yield scrapy.Request(url, self.parse,  headers=self.headers)



