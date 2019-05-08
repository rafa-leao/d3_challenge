import requests

from utils.get_url import get_url
from utils.anchor_content import anchor_content


def all_site_paths(paths):

	paths_found = []

	for path in paths:

		path_result = anchor_content(get_url('https://scrapethissite.com{}'.format(path)))

		for single_path in path_result:

			if single_path.startswith('/'):

				paths_found.append(path)

	# remove duplicates
	return list(dict.fromkeys(paths_found))
