import scrapy

class Scrape(scrapy.Spider):
	name = "book_scrape"

	def start_requests(self):

		urls = ['http://books.toscrape.com/']

		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):

		data = response.css("ol.row")

		for q in data.css("article.product_pod"):
			image_url = q.css("div.image_container img").attrib['src']
			book_title = q.css("div.image_container img").attrib['alt']
			book_price = q.css("div.product_price p::text").get()

			yield{
				'image_url':image_url,
				'book_title':book_title,
				'product_price':book_price
			}
		next_page = response.css("li.next a").attrib['href']
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page,callback=self.parse)