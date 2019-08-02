from scraper.robot import Robot

if __name__ == '__main__':

	print("-*-------------*-")
	print("-* Scraping... *-")
	print("-*-------------*-")


	paths = Robot('https://scrapethissite.com/pages', ['/ ', '/lessons/', '/faq/']).map_site()
	
	print("-*-------------*-------------*-------------*-------------*-------------*-")
	print("ALL ALLOWED PATHS ==> ", paths)
	print("-*-------------*-------------*-------------*-------------*-------------*-")


	print(Robot('https://scrapethissite.com/pages', ['/ ', '/lessons/', '/faq/']).path_assets_catcher(paths))

	print("-*-------------*-------------*-------------*-------------*-------------*-")
	print("-*   Copy this huge return and paste on: http://jsonviewer.stack.hu/   *-")
	print("-*-------------*-------------*-------------*-------------*-------------*-")
