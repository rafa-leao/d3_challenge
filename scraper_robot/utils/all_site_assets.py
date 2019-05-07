from bs4 import BeautifulSoup
import requests


def all_site_assets(paths):

	assets_atached = []

	for path in paths:

		assets_atached.append("The assets of {} is:".format(path))

		try:

			print('Trying to get {}'.format(path))
			site_response = requests.get('https://scrapethissite.com{}'.format(path)).content

		except:

			print("An error ocurred while trying getting the url passed")
		
		print('Parsing in {} HTML'.format(path))
		site_content = BeautifulSoup(site_response, "html.parser")

		js_files = site_content.find_all('script')
		for js_file in js_files:
			# it is not going to catch javascript wrotten in the bare HTML file
			js_file = js_file.attrs["src"] if "src" in js_file.attrs else ''
			print("Cathing js files from {}".format(path))
			assets_atached.append(js_file)

		css_files = site_content.find_all('link')
		for css_file in css_files:
			# it is not going to catch css wrotten in the bare HTML file
			css_file = css_file.attrs["href"] if 'rel="stylesheet"' in css_file.attrs else ''
			print("Cathing css files from {}".format(path))
			assets_atached.append(css_file)

		img_files = site_content.find_all('img')
		for img_file in img_files:
			# it is not going to catch <link rel="icon"> yet
			img_file = img_file.attrs["src"] if "src" in img_file.attrs else ''
			print("Cathing img files from {}".format(path))
			assets_atached.append(img_file)


	return assets_atached
