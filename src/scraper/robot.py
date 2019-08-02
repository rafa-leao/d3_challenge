from utils.get_url import get_url
from utils.url_checker import url_checker
from utils.path_checker import path_checker
from utils.anchor_content import anchor_content
from utils.all_site_paths import all_site_paths
from utils.assets_from_path import assets_from_path


class Robot:

	def __init__(self, 
				 url_site = 'https://scrapethissite.com/pages',
				 url_site_disallowed_path = ['/ ', '/lessons/', '/faq/'] ):

		self.url_site 				  = url_site
		self.url_site_disallowed_path = url_site_disallowed_path
		
	def paths_catcher(self):

		url_validator = url_checker(self.url_site,
									self.url_site_disallowed_path)

		if url_validator:
			

			site_anchors_content = anchor_content(get_url(self.url_site))
			print('We got all paths in {}. Now we will crawl through them and map the site!'
				  .format(self.url_site)
			)

			return all_site_paths(
				path_checker(site_anchors_content, self.url_site_disallowed_path)
			)

		else:

			print("Sorry, the path in the site which you trying to access is not allowed!")

	def path_assets_catcher(self, paths):

		assets_found = []

		for path in paths:

			html_content = get_url('https://scrapethissite.com{}'.format(path))

			js_found  = html_content.find_all('script')
			css_found = html_content.find_all('link')
			img_found = html_content.find_all('img')
			

			assets_found.append(assets_from_path(path, js_found, css_found, img_found))

		return assets_found
