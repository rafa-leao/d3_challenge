def anchor_content(site_content):

	site_anchors_content = []

	links = site_content.find_all('a')

	for link in links:
		link = link.attrs["href"] if "href" in link.attrs else ''
		site_anchors_content.append(link)

	return site_anchors_content
