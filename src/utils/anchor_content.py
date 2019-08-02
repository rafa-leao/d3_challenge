from utils.get_url import get_url


def anchor_content(url_site, paths_not_allowed):

	site_content = get_url(url_site)

	links = site_content.find_all('a')

	# get all anchors
	site_anchors = []

	for link in links:
		link = link.attrs["href"] if "href" in link.attrs else ''
		site_anchors.append(link)

	# Filter anchors to return only allowed paths
	paths = []

	for path in site_anchors:

		if path not in paths_not_allowed:
			paths.append(path)

	return paths
