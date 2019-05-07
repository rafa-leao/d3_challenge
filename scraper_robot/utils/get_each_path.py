from bs4 import BeautifulSoup
import requests

from utils.anchor_content import anchor_content

def get_each_path(url_site):
	
	try:

		site_response = requests.get(url_site, timeout=5).content

	except:

		print("An error ocurred while trying getting the url passed")

	site_content = BeautifulSoup(site_response, "html.parser")

	return anchor_content(site_content)
