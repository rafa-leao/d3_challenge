from utils.get_url import get_url
from utils.url_checker import url_checker
from utils.anchor_content import anchor_content
from utils.assets_from_path import assets_from_path


class Robot:

	def __init__(self, url_site, paths_not_allowed):

		self.url_site 		   = url_site
		self.paths_not_allowed = paths_not_allowed


	def map_site(self):

		# Checks if the path followed by the given site is not forbidden
		if url_checker(self.url_site, self.paths_not_allowed):

			paths = anchor_content(self.url_site, self.paths_not_allowed)

			print('We got all the anchors from {}. Now we will crawl through them and map the site!'.format(self.url_site))
			print("-*-------------*-------------*-------------*-------------*-------------*-------------*-------------*-------------*-")

			# Crawl through the site and map it
			paths_found = []

			for path in paths:

				path_result = anchor_content('https://scrapethissite.com{}'.format(path), self.paths_not_allowed)

				for single_path in path_result:

					if single_path.startswith('/'):
						paths_found.append(path)

			# return the mapped site and remove duplicates
			return list(dict.fromkeys(paths_found))

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
