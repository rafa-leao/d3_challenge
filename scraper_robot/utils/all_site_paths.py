import requests

from utils.get_each_path import get_each_path


def all_site_paths(paths):

	paths_found = []

	for path in paths:

		path_result = get_each_path('https://scrapethissite.com{}'.format(path))

		for single_path in path_result:

			if single_path.startswith('/'):

				paths_found.append(path)

	# remove duplicates
	return list(dict.fromkeys(paths_found))
