from utils.url_checker import url_checker
from utils.path_checker import path_checker
from utils.get_each_path import get_each_path
from utils.all_site_paths import all_site_paths


class Robot:

	def __init__(self, 
				 url_site,
				 url_site_disallowed_path = ['/ ', '/lessons/', '/faq/'] ):

		self.url_site 				  = url_site
		self.url_site_disallowed_path = url_site_disallowed_path
		
	def paths_catcher(self):

		url_validator = url_checker(self.url_site,
									self.url_site_disallowed_path)

		if url_validator:
			
			site_anchors_content = get_each_path(self.url_site)

			return all_site_paths(
				path_checker(site_anchors_content, self.url_site_disallowed_path)
			)

		else:

			print("Sorry, the path in the site wich you trying to access is disallowed!")
