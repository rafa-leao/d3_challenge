from bs4 import BeautifulSoup
import requests

from utils.url_checker import url_checker

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

			site_content_urls = []

			links = site_content.find_all('a')
			for link in links:
				link = link.attrs["href"] if "href" in link.attrs else ''
				site_content_urls.append(link)

			paths = []

			for path in site_content_urls:

				if path not in self.url_site_disallowed_path:

					paths.append(path)

			return paths

		else:

			print("Sorry, the path in the site wich you trying to access is disallowed!")
