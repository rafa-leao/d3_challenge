from bs4 import BeautifulSoup
import requests


def get_url(url_site):
	
	try:

		print('Trying to get {}'.format(url_site))
		site_response = requests.get(url_site, timeout=5).content

	except:

		print("An error ocurred while trying getting the url passed")

	return BeautifulSoup(site_response, "html.parser")
