from bs4 import BeautifulSoup
import requests

from utils.url_checker import url_checker
from utils.path_checker import path_checker
from utils.anchor_content import anchor_content


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

			try:

				site_response = requests.get(self.url_site, timeout=5).content

			except:

				print("An error ocurred while trying getting the url passed")

			site_content = BeautifulSoup(site_response, "html.parser")

			site_anchors_content = anchor_content(site_content)

			return path_checker(site_anchors_contents, self.url_site_disallowed_path)

		else:

			print("Sorry, the path in the site wich you trying to access is disallowed!")
