def anchor_content(site_content):

	site_content_urls = []

	links = site_content.find_all('a')

	for link in links:
		link = link.attrs["href"] if "href" in link.attrs else ''
		site_content_urls.append(link)

	return site_content_urls
