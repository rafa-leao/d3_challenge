def  path_checker(site_anchors_content, url_site_disallowed_path):

	paths = []

	for path in site_anchors_content:

		if path not in url_site_disallowed_path:

			paths.append(path)

	return paths