def  path_checker(site_content_url, url_site_disallowed_path):

	paths = []

	for path in site_content_url:

		if path not in url_site_disallowed_path:

			paths.append(path)

	return paths